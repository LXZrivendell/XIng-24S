import base
from ch2b import NOT_EXPECTED_2b

EXPECTED_3b = [
    # ch3b_yield0
    "Test write A OK3050!",

    # ch3b_yield1
    "Test write B OK3050!",

    # ch3b_yield2
    "Test write C OK3050!",
]

if __name__ == "__main__":
    base.test(EXPECTED_3b, NOT_EXPECTED_2b)
