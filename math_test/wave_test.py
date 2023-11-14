import math
import numpy as np

from math_core.math_core import *
from math_core.math_run_helper import Plotter2D


def sin_wave_test():
    plotter2d = Plotter2D()

    x = np.arange(0, 6.28, 0.01)
    y1 = sin_func_2d(x, 2.0 * math.pi, 0.3)
    y2 = sin_func_2d(x, 1.0 * math.pi, 0.3)
    y3 = sin_func_2d(x, 0.5 * math.pi, 1.0)
    y4 = y1 + y2 + y3

    plotter2d.add_data_to_plotter(x, y1)
    plotter2d.add_data_to_plotter(x, y2)
    plotter2d.add_data_to_plotter(x, y3)
    plotter2d.add_data_to_plotter(x, y4)

    plotter2d.draw()


def wave_test(run: bool = True):
    if run:
        sin_wave_test()
