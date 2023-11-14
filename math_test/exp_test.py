import math

from math_core.math_core import *


def exp_func(base_num: float, dt: float = 0.001):
    val = (math.pow(base_num, dt) - 1) / dt
    logging.info("base:{}, dt:{}, val:{}".format(base_num, dt, val))


def exp_test(run: bool = True):
    if run:
        dt = 1e-9
        for b in range(1, 10):
            exp_func(b, dt)
        exp_func(math.e, dt)
