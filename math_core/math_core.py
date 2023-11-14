import os
import sys
import glog
import math
import random
import logging
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def sin_func_2d(x: np.ndarray, omega: float = 2 * math.pi, amplitude: float = 1.0, phase: float = 0.0) -> np.ndarray:
    y: np.ndarray = np.zeros(x.size)
    for i in range(x.size):
        y[i] = amplitude * math.sin(x[i] * omega + phase)
    return y
