import base

EXPECTED_2b = [
    # ch2b_hello_world
    "Hello, world from user mode program!",

    # ch2b_power_3
    "Test power_3 OK84082852733355531910260!",

    # ch2b_power_5
    "Test power_5 OK84082852733355531910260!",

    # ch2b_power_7
    "Test power_7 OK84082852733355531910260!",
]

NOT_EXPECTED_2b = [
    "FAIL: T.T",
]

if __name__ == "__main__":
    base.test(EXPECTED_2b, NOT_EXPECTED_2b)
