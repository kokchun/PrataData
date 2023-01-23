#%%
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

    def set_ticklabel_color(self, color=GRAY1):
        self.ax.xaxis.set_tick_params(labelcolor=color)
        self.ax.yaxis.set_tick_params(labelcolor=color)

        return self


#%%
