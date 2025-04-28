import base
from ch6b import EXPECTED_6b
from ch5 import EXPECTED_5, NOT_EXPECTED_4b

EXPECTED_6 = list(set(EXPECTED_5 + EXPECTED_6b + [
    # ch6_file0
    "Test file0 OK526341187656213652495969263464193050!",

    # ch6_file1
    "Test fstat OK526341187656213652495969263464193050!",

    # ch6_file2
    "Test link OK526341187656213652495969263464193050!",

    # ch6_file3
    "Test mass open/unlink OK526341187656213652495969263464193050!",
]))

EXPECTED_6 = list(set(EXPECTED_6) - set(["Test set_priority OK526341187656213652495969263464193050!"]))

if __name__ == "__main__":
    base.test(EXPECTED_6, NOT_EXPECTED_4b)