//! Process management syscalls
use crate::{
    config::MAX_SYSCALL_NUM,
    task::{
        change_program_brk, exit_current_and_run_next, suspend_current_and_run_next, TaskStatus, TASK_MANAGER,
    },
};

use crate::timer::get_time_us;
//use crate::mm::PageTable;
//use crate::mm::{VirtAddr, VirtPageNum, PAGE_SIZE, PAGE_SIZE_BITS};
//use core::mem::size_of;

use crate::mm::PageTable;
use crate::mm::VirtAddr;
use crate::config::{PAGE_SIZE, PAGE_SIZE_BITS};
use crate::task::current_user_token;

#[repr(C)]
#[derive(Debug)]
pub struct TimeVal {
    pub sec: usize,
    pub usec: usize,
}

/// Task information
#[allow(dead_code)]
pub struct TaskInfo {
    /// Task status in it's life cycle
    status: TaskStatus,
    /// The numbers of syscall called by task
    syscall_times: [u32; MAX_SYSCALL_NUM],
    /// Total running time of task
    time: usize,
}

/// task exits and submit an exit code
pub fn sys_exit(_exit_code: i32) -> ! {
    trace!("kernel: sys_exit");
    exit_current_and_run_next();
    panic!("Unreachable in sys_exit!");
}

/// current task gives up resources for other tasks
pub fn sys_yield() -> isize {
    trace!("kernel: sys_yield");
    suspend_current_and_run_next();
    0
}

/// 系统调用：获取当前时间到用户传入的 TimeVal*
pub fn sys_get_time(ts: *mut TimeVal, _tz: usize) -> isize {
        trace!("kernel: sys_get_time");
        let us = get_time_us();
        // 把用户空间指针翻译到内核可写指针
        let token = current_user_token();
        let va = ts as usize;
        let vpn = VirtAddr(va).floor();
        let pte = match PageTable::from_token(token).translate(vpn) {
            Some(p) if p.is_valid() => p,
            _ => return -1,
        };
        // 页内偏移
        let offset = va & (PAGE_SIZE - 1);
        // 转成物理地址
        let pa = (pte.ppn().0 << PAGE_SIZE_BITS) + offset;
        unsafe {
            let ptr: *mut TimeVal = pa as *mut TimeVal;
            *ptr = TimeVal { sec: us / 1_000_000, usec: us % 1_000_000 };
        }
        0
    }

/// 系统调用：查询当前任务信息到用户传入的 TaskInfo*
pub fn sys_task_info(ti: *mut TaskInfo) -> isize {
        trace!("kernel: sys_task_info");
        let token = current_user_token();
        let va = ti as usize;
        let vpn = VirtAddr(va).floor();
        let pte = match PageTable::from_token(token).translate(vpn) {
            Some(p) if p.is_valid() => p,
            _ => return -1,
        };
        let offset = va & (PAGE_SIZE - 1);
        let pa = (pte.ppn().0 << PAGE_SIZE_BITS) + offset;
        // 拷贝数据
        let counts = TASK_MANAGER.get_sys_call_times();
        let elapsed_ms = get_time_us() / 1000;
        unsafe {
            let ptr: *mut TaskInfo = pa as *mut TaskInfo;
            *ptr = TaskInfo {
                status: TaskStatus::Running,
                syscall_times: counts,
                time: elapsed_ms,
            };
        }
        0
    }

/// 系统调用：匿名映射
pub fn sys_mmap(start: usize, len: usize, port: usize) -> isize {
        trace!("kernel: sys_mmap start={:#x}, len={}, port={:#x}", start, len, port);
        crate::task::sys_mmap(start, len, port)
    }

/// 系统调用：匿名解除映射
pub fn sys_munmap(start: usize, len: usize) -> isize {
        trace!("kernel: sys_munmap start={:#x}, len={}", start, len);
        crate::task::sys_munmap(start, len)
    }
/// change data segment size
pub fn sys_sbrk(size: i32) -> isize {
    trace!("kernel: sys_sbrk");
    if let Some(old_brk) = change_program_brk(size) {
        old_brk as isize
    } else {
        -1
    }
}
