import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fcc-forum-pageviews.csv")


df['date'] = pd.to_datetime(df['date'])


df = df.set_index('date')

lower_limit = df['value'].quantile(0.025)
upper_limit = df['value'].quantile(0.975)

df = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]


def draw_line_plot():

    df_line = df.copy()

    plt.figure(figsize=(12, 5))
    plt.plot(df_line.index, df_line['value'])


    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")


    fig = plt.gcf()
    fig.savefig("line_plot.png")
    return fig

def draw_bar_plot():

    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean()
    df_grouped = df_grouped.unstack()

 
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    df_grouped.columns = months

    # Plot
    df_grouped.plot(kind='bar', figsize=(10, 7))

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    fig = plt.gcf()
    fig.savefig("bar_plot.png")
    return fig

def draw_box_plot():

    df_box = df.copy()

    df_box = df_box.reset_index()

    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.boxplot(
        x='year',
        y='value',
        data=df_box,
        ax=axes[0]
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(
        x='month',
        y='value',
        data=df_box,
        order=month_order,
        ax=axes[1]
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig