import matplotlib.pyplot as plt 
from pathlib import Path
import pandas as pd

data_path = Path(__file__).parents[1] / "data"

class StoryChart:
    
    print("hej")


if __name__ == "__main__":
    df = pd.read_csv(data_path/"co2_annmean_mlo.csv", skiprows=43)
    print(df)
