import copy
from abc import abstractmethod

from math_core.math_core import *


class ComplexDrawer:
    """
    used to draw complex number
    """

    def __init__(self, plot_name: str = ""):
        self.__axle = plt.axes()
        self.__complex_list: [np.complex_] = []
        self.__plot_name = plot_name
        self.__axle.set_title(self.__plot_name)

    def add_complex_to_draw(self, complex_number: np.complex_):
        self.__complex_list.append(complex_number)

    def remove_complex(self, complex_number: np.complex_):
        self.__complex_list.remove(complex_number)

    def draw(self):
        for complex_number in self.__complex_list:
            point = (np.real(complex_number), np.imag(complex_number))
            point_text = "({:.3f},{:.3f})".format(point[0], point[1])
            self.__axle.arrow(0, 0, point[0], point[1], head_width=0.01, head_length=0.03,
                              fc='k', ec='k')
            plt.annotate(point_text, point)
        plt.show()


class PlotData:
    def __init__(self, x: np.ndarray, y: np.ndarray, z: np.ndarray):
        self.data = {"x": copy.copy(x), "y": copy.copy(y), "z": copy.copy(z)}

    def get_data(self):
        return self.data


class PlotterBase:
    def __init__(self, plot_name=""):
        self.figure = plt.figure()
        self.total_rows = 1
        self.row_index = 1
        self.col_index = 1
        self.sub_plots = []

        self.plot_data: [PlotData] = []
        self.figure.suptitle(plot_name)
        self.color_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                           '#bcbd22', '#17becf']

    def add_data_to_plotter(self, x: np.ndarray, y: np.ndarray, z: [float] = np.zeros(1)):
        self.plot_data.append(PlotData(x, y, z))

    @abstractmethod
    def draw(self):
        raise "not implemented error."


class Plotter2D(PlotterBase):
    def __init__(self, plot_name=""):
        super().__init__(plot_name)

    def draw(self):
        self.total_rows = len(self.plot_data)
        for plot_data in self.plot_data:
            data_dict = plot_data.get_data()
            one_plot = self.figure.add_subplot(self.total_rows, self.col_index, self.row_index)
            self.sub_plots.append(one_plot)
            one_plot.plot(data_dict["x"], data_dict["y"], color=random.choice(self.color_list))
            self.row_index += 1
        plt.show()


class MathRunHelper:
    def __init__(self):
        self.name: str = "MathRunHelper"

    @staticmethod
    def run(func, *args):
        func(*args)

    @staticmethod
    def create_complex(real_part: float, imag_part: float) -> np.complex_:
        logging.info("real part:{}, imagine part:{}".format(real_part, imag_part))
        return complex(real_part, imag_part)

    @staticmethod
    def create_complex_from_theta(theta: float) -> np.complex_:
        logging.info("theta[deg]:{}".format(theta / math.pi * 180.0))
        return MathRunHelper.create_complex(math.cos(theta), math.sin(theta))

    @staticmethod
    def print_complex_number(complex_0: np.complex_):
        logging.info("real part:{}, imagine part:{}".format(np.real(complex_0), np.imag(complex_0)))
