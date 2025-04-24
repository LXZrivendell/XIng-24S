import base

EXPECTED_3 = [
    # ch3_sleep
    r"get_time OK2852733355531910260! (\d+)",
    "Test sleep OK2852733355531910260!",

    # ch3_sleep1
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed2852733355531910260!",

    # ch3_taskinfo
    "string from task info test",
    "Test task info OK2852733355531910260!",
]

if __name__ == "__main__":
    base.test(EXPECTED_3)
