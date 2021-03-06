import datetime as Dt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.stats import gaussian_kde


def fyear2datetime(year):

    iyear = int(year)
    y = Dt.datetime(iyear, 1, 1)
    yn = Dt.datetime(iyear + 1, 1, 1)
    dt = yn - y
    return y + (year - iyear) * dt


def style_diff(df, df_orig):

    style = {True: "", False: "color: red; background-color: yellow"}
    df_style = (df == df_orig).replace(style)
    return df.style.apply(lambda x: df_style, axis=None)


def resample_time(df1, df_ref):

    df2 = pd.DataFrame(index=df_ref.index, columns=df1.columns)
    df3 = pd.concat([df1, df2], copy=True)
    df3 = df3.sort_index(axis=0).interpolate(method="linear").dropna()
    df3 = df3[df3.index.isin(df_ref.index)]

    return df3


def plot_gaussien_kde(x, y):
    # plot 2 Ch_xxx at a given L

    # Calculate the point density
    xy = np.vstack([x, y])
    z = gaussian_kde(xy)(xy)

    # Sort the points by density, so that the densest points are plotted last
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]

    fig, ax = plt.subplots()
    ax.scatter(x, y, c=z, s=50)
    plt.show()
