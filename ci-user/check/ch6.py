import base
from ch6b import EXPECTED_6b
from ch5 import EXPECTED_5, NOT_EXPECTED_4b

EXPECTED_6 = list(set(EXPECTED_5 + EXPECTED_6b + [
    # ch6_file0
    "Test file0 OK2852733355531910260!",

    # ch6_file1
    "Test fstat OK2852733355531910260!",

    # ch6_file2
    "Test link OK2852733355531910260!",

    # ch6_file3
    "Test mass open/unlink OK2852733355531910260!",
]))

EXPECTED_6 = list(set(EXPECTED_6) - set(["Test set_priority OK2852733355531910260!"]))

if __name__ == "__main__":
    base.test(EXPECTED_6, NOT_EXPECTED_4b)