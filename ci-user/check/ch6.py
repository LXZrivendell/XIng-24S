import base
from ch6b import EXPECTED_6b
from ch5 import EXPECTED_5, NOT_EXPECTED_4b

EXPECTED_6 = list(set(EXPECTED_5 + EXPECTED_6b + [
    # ch6_file0
    "Test file0 OK1937!",

    # ch6_file1
    "Test fstat OK1937!",

    # ch6_file2
    "Test link OK1937!",

    # ch6_file3
    "Test mass open/unlink OK1937!",
]))

EXPECTED_6 = list(set(EXPECTED_6) - set(["Test set_priority OK1937!"]))

if __name__ == "__main__":
    base.test(EXPECTED_6, NOT_EXPECTED_4b)