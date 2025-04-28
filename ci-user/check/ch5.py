import base
from ch5b import EXPECTED_5b, NOT_EXPECTED_4b
from ch4 import EXPECTED_4

EXPECTED_5 = EXPECTED_4 + [
    # ch5_spawn0
    "Test spawn0 OK421285257429142!",

    # ch5_spawn1
    "Test wait OK421285257429142!",
    "Test waitpid OK421285257429142!",

    # ch5_setprio
    "Test set_priority OK421285257429142!",
]

EXPECTED_5 = list(set(EXPECTED_5) - set([
    "string from task info test",
    "Test task info OK421285257429142!",
]))

if __name__ == "__main__":
    base.test(EXPECTED_5, NOT_EXPECTED_4b)