import base
from ch2b import NOT_EXPECTED_2b

EXPECTED_3b = [
    # ch3b_yield0
    "Test write A OK10260!",

    # ch3b_yield1
    "Test write B OK10260!",

    # ch3b_yield2
    "Test write C OK10260!",
]

if __name__ == "__main__":
    base.test(EXPECTED_3b, NOT_EXPECTED_2b)
