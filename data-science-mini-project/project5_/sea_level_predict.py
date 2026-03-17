import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
   
    df = pd.read_csv("epa-sea-level.csv")

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    result = linregress(x, y)

    slope = result.slope
    intercept = result.intercept

    future_years = list(range(int(x.min()), 2051))

    predicted_values = []
    for year in future_years:
        predicted_y = slope * year + intercept
        predicted_values.append(predicted_y)

    plt.plot(future_years, predicted_values, label="Fit: All Data")

    df_recent = df[df['Year'] >= 2000]

    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']

    result_recent = linregress(x_recent, y_recent)

    slope_recent = result_recent.slope
    intercept_recent = result_recent.intercept

    future_years_recent = list(range(2000, 2051))

    predicted_recent = []
    for year in future_years_recent:
        predicted_y = slope_recent * year + intercept_recent
        predicted_recent.append(predicted_y)

    plt.plot(future_years_recent, predicted_recent, label="Fit: Since 2000")

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.legend()

    fig = plt.gcf()
    fig.savefig("sea_level_plot.png")

    return fig