import gif
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from config.constants import SIM_DAYS


@gif.frame
def plot_comparison(
    grid_a: np.ndarray,
    ts_a: pd.Series,
    grid_b: np.ndarray,
    ts_b: pd.Series,
):
    fig = plt.figure(figsize=(16, 9), layout='constrained', dpi=200)
    spec = fig.add_gridspec(20, 10)

    ax1 = fig.add_subplot(spec[0:17, 0:5])
    ax1.set_title('No Quarantine')

    # plot heatmap of grid
    sns.heatmap(
        grid_a,
        ax=ax1,
        cbar=False,
        cmap='magma',
        square=True,
        linewidths=0.1,
        linecolor='black',
        vmin=-1,
        vmax=3,
        xticklabels=False,
        yticklabels=False,
    )

    ax2 = fig.add_subplot(spec[0:17, 5:10])
    ax2.set_title('Quarantine')

    # plot heatmap of grid
    sns.heatmap(
        grid_b,
        ax=ax2,
        cbar=False,
        cmap='magma',
        square=True,
        linewidths=0.1,
        linecolor='black',
        vmin=-1,
        vmax=3,
        xticklabels=False,
        yticklabels=False,
    )

    ax3 = fig.add_subplot(spec[17:20, 3:7])
    ax3.set_title('Infected distribution over time')

    # plot time series, max x is SIM_DAYS

    ax3.plot(ts_a, color='red', label='No Quarantine')
    ax3.plot(ts_b, color='blue', label='Quarantine')
    ax3.set_xlabel('Days')
    ax3.set_ylabel('Infected, %')
    ax3.legend()

    ax3.set_xlim(0, SIM_DAYS)
    ax3.set_ylim(0, 27)

    fig.suptitle('Free spread vs. isolated subgroups')
