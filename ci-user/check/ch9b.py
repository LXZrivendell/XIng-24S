import base
from ch6b import EXPECTED_6b, NOT_EXPECTED_4b

EXPECTED_9b = EXPECTED_6b + [
    # ch7b_pipetest
    "pipetest passed421285257429142!",

    # ch8b_mpsc_sem
    "mpsc_sem passed421285257429142!",

    # ch8b_phil_din_mutex
    "philosopher dining problem with mutex test passed421285257429142!",

    # ch8b_race_adder_mutex_spin
    "race adder using spin mutex test passed421285257429142!",

    # ch8b_sync_sem
    "sync_sem passed421285257429142!",

    # ch8b_test_condvar
    "test_condvar passed421285257429142!",

    # ch8b_threads_arg
    "threads with arg test passed421285257429142!",

    # ch8b_threads
    "threads test passed421285257429142!",
]

EXPECTED_9b = list(set(EXPECTED_9b) - set(["Test sbrk almost OK421285257429142!"]))

if __name__ == "__main__":
    base.test(EXPECTED_9b, NOT_EXPECTED_4b)
