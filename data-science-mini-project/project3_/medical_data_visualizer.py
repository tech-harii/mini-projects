import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("medical_examination.csv")



overweight_list = []

for i in range(len(df)):
    height_m = df.loc[i, 'height'] / 100  # to convert cm to meters
    weight = df.loc[i, 'weight']

    bmi = weight / (height_m * height_m)

    if bmi > 25:
        overweight_list.append(1)
    else:
        overweight_list.append(0)

df['overweight'] = overweight_list

for i in range(len(df)):
    if df.loc[i, 'cholesterol'] == 1:
        df.loc[i, 'cholesterol'] = 0
    else:
        df.loc[i, 'cholesterol'] = 1

for i in range(len(df)):
    if df.loc[i, 'gluc'] == 1:
        df.loc[i, 'gluc'] = 0
    else:
        df.loc[i, 'gluc'] = 1


def draw_cat_plot():

    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size()
    df_cat = df_cat.reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})


    graph = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )

    fig = graph.fig
    return fig



def draw_heat_map():

    df_heat = df[df['ap_lo'] <= df['ap_hi']]

    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]

    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    # Correlation
    corr = df_heat.corr()

    mask = np.triu(np.ones(corr.shape)).astype(bool)

    # Ploting
    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True
    )

    return fig