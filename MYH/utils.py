from dataclasses import dataclass
import matplotlib.pyplot as plt
from colors import *


@dataclass
class PlotSettings:
    ax: plt.axes

    def remove_borders(self):
        self.ax.xaxis.set_ticks_position("none")
        self.ax.yaxis.set_ticks_position("none")

        for spine in self.ax.spines.values():
            spine.set_visible(False)

        return self

    def remove_yaxis(self):
        self.ax.get_yaxis().set_visible(False)
        return self

    def set_ticklabel_color(self, color=GRAY1):
        self.ax.xaxis.set_tick_params(labelcolor=color)
        self.ax.yaxis.set_tick_params(labelcolor=color)
        return self

    def set_labels(
        self,
        xlabel="",
        ylabel="",
        xlabel_position=(0.045, -0.1),
        ylabel_position=(0.01, 0.93),
    ):
        self.ax.set_xlabel(xlabel, color=GRAY2)
        self.ax.xaxis.set_label_coords(*xlabel_position)

        self.ax.set_ylabel(ylabel, color=GRAY2).set_rotation(0)
        self.ax.yaxis.set_label_coords(*ylabel_position)
        return self


@dataclass
class AnnotateLine:
    ax: plt.axes

    def annoatate_line(
        self, indexes, values, x_offset=0, y_offset=0, symbol_character="", color=None
    ):
        for index, value in zip(indexes, values):
            self.ax.annotate(
                f"{value:.0f}{symbol_character}",
                xy=(index + x_offset, value + y_offset),
                color=color,
            )

        return self
