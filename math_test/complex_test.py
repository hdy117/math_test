import math
import logging
import numpy as np

from math_core.math_core import *
from math_core.math_run_helper import MathRunHelper, ComplexDrawer


def demo_base_func():
    theta: float = 30.0 / 180.0 * math.pi
    complex_number = MathRunHelper.create_complex(math.cos(theta), math.sin(theta))

    complex_drawer = ComplexDrawer()
    complex_drawer.add_complex_to_draw(complex_number)

    MathRunHelper.run(complex_drawer.draw)


def add_func(complex_0: np.complex_, complex_1: np.complex_):
    complex_drawer = ComplexDrawer("add")

    complex_drawer.add_complex_to_draw(complex_0)
    complex_drawer.add_complex_to_draw(complex_1)
    complex_drawer.add_complex_to_draw(complex_0 + complex_1)

    MathRunHelper.run(complex_drawer.draw)


def conjugate_func(complex_0: np.complex_):
    complex_drawer = ComplexDrawer("conjugate")

    complex_drawer.add_complex_to_draw(complex_0)
    complex_drawer.add_complex_to_draw(complex_0.conjugate())

    MathRunHelper.run(complex_drawer.draw)


def multiply_func(complex_0: np.complex_, complex_1: np.complex_):
    complex_drawer = ComplexDrawer("multiply")

    complex_drawer.add_complex_to_draw(complex_0)
    complex_drawer.add_complex_to_draw(complex_1)
    complex_drawer.add_complex_to_draw(complex_0 * complex_1)

    MathRunHelper.run(complex_drawer.draw)


def divide_func(complex_0: np.complex_, complex_1: np.complex_):
    complex_drawer = ComplexDrawer("divide")

    complex_drawer.add_complex_to_draw(complex_0)
    complex_drawer.add_complex_to_draw(complex_1)
    complex_drawer.add_complex_to_draw(complex_0 * complex_1.conjugate())

    MathRunHelper.run(complex_drawer.draw)


def normal_func(complex_0: np.complex_):
    logging.info("normal:{}".format(complex_0 * complex_0.conjugate()))


def complex_test(run: bool = True):
    if run:
        # prepare complex number
        theta_15: float = 15.0 / 180.0 * math.pi
        theta_30: float = 30.0 / 180.0 * math.pi
        theta_45: float = 45.0 / 180.0 * math.pi

        complex_15 = MathRunHelper.create_complex_from_theta(theta_15)
        complex_30 = MathRunHelper.create_complex_from_theta(theta_30)
        complex_45 = MathRunHelper.create_complex_from_theta(theta_45)

        # print complex
        MathRunHelper.print_complex_number(np.log(0.7853981633974483j, dtype=np.complex_))

        # add complex number
        add_func(complex_30, complex_15)

        # multiply complex number
        multiply_func(complex_15, complex_30)

        # conjugate complex
        conjugate_func(complex_30)

        # divide complex
        divide_func(complex_45, complex_15)

        # normal function
        normal_func(complex_30)
        normal_func(complex_15)
        normal_func(complex_45)
