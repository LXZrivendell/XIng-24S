//! Types related to task management
#[allow(unused)]
use super::TaskContext;
//use crate::config::MAX_APP_NUM;
use crate::config::MAX_SYSCALL_NUM;

/// The task control block (TCB) of a task.
#[derive(Copy, Clone)]
pub struct TaskControlBlock {
    /// The task status in it's lifecycle
    pub task_status: TaskStatus,
    /// The task context
    pub task_cx: TaskContext,
    /// ch3, The time when the task first starts
    pub task_first_start_time: isize,
    /// ch3, The numbers of syscall called by task
    pub syscall_times: [u32; MAX_SYSCALL_NUM],
     /// ch3,
    pub switch_time: usize,
     /// ch3,
    pub user_time: usize,
     /// ch3,
    pub kernel_time: usize,
}

/// The status of a task
#[derive(Copy, Clone, PartialEq)]
pub enum TaskStatus {
    /// uninitialized
    UnInit,
    /// ready to run
    Ready,
    /// running
    Running,
    /// exited
    Exited,
}
