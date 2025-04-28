import base

EXPECTED_3 = [
    # ch3_sleep
    r"get_time OK526341187656213652495969263464193050! (\d+)",
    "Test sleep OK526341187656213652495969263464193050!",

    # ch3_sleep1
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed526341187656213652495969263464193050!",

    # ch3_taskinfo
    "string from task info test",
    "Test task info OK526341187656213652495969263464193050!",
]

if __name__ == "__main__":
    base.test(EXPECTED_3)
