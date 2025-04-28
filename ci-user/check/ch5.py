import base
from ch5b import EXPECTED_5b, NOT_EXPECTED_4b
from ch4 import EXPECTED_4

EXPECTED_5 = EXPECTED_4 + [
    # ch5_spawn0
    "Test spawn0 OK526341187656213652495969263464193050!",

    # ch5_spawn1
    "Test wait OK526341187656213652495969263464193050!",
    "Test waitpid OK526341187656213652495969263464193050!",

    # ch5_setprio
    "Test set_priority OK526341187656213652495969263464193050!",
]

EXPECTED_5 = list(set(EXPECTED_5) - set([
    "string from task info test",
    "Test task info OK526341187656213652495969263464193050!",
]))

if __name__ == "__main__":
    base.test(EXPECTED_5, NOT_EXPECTED_4b)