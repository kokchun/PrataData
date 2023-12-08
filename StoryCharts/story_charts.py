import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

data_path = Path(__file__).parents[1] / "data"
styles_path = Path(__file__).parent / "styles"


class StoryChart:
    def __init__(self) -> None:
        plt.style.use(styles_path / "base.mplstyle")

    def _set_labels(self, title, xlabel, ylabel):
        self.ax.set_xlabel(xlabel, loc="left")
        self.ax.set_ylabel(ylabel, loc="top")
        self.ax.set_title(title, loc="left", pad=15)

    def Line(self, x, y, color="#0c4a6e", **label_kwargs):
        self.fig, self.ax = plt.subplots()
        self.ax.plot(x, y, color=color)
        self._set_labels(**label_kwargs)
        self.fig.tight_layout()
        plt.show()

    def Bar(self, x, y, colors="#0c4a6e", **label_kwargs):
        self.fig, self.ax = plt.subplots()
        self.ax.bar(x, y, color=colors)
        self.ax.tick_params(axis='x', colors="#1f2937")
        self._set_labels(**label_kwargs)
        plt.show()

# manual testing
if __name__ == "__main__":
    df = pd.read_csv(data_path / "co2_annmean_mlo.csv", skiprows=43)

    sc = StoryChart()
    title = "The annual mean of CO$_2$ emissions measured in Mauna Loa has \nincreased every year since 1959"
    sc.Line(
        df["year"],
        df["mean"],
        title=title,
        color="#e11d48",
        xlabel="YEARS FROM 1959",
        ylabel="CO$_2$ MOLE FRACTON IN PPM",
    )

    sc.Line()

    sc.fig.savefig(Path(__file__).parent / "line.png", dpi=200)
