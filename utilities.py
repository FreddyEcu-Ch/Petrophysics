# Import Pyhton Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lasio
import welly
from pathlib import Path
import streamlit as st


# Function to plot with Welly and Matplotlib any log curve
def curvas_logs(curvas, log, inicio, final):
    fig, axes = plt.subplots(1, len(curvas), figsize=(20,10))
    for ind, curva in enumerate(curvas):
        segmento = log.data[curva].to_basis(start=inicio, stop=final)
        if curva == 'SAND_FLAG':
            segmento.plot_2d(ax= axes[ind])
        else:
            segmento.plot(ax=axes[ind])
        axes[ind].set_title(curva)
    axes[0].set_ylabel('Depth (m)', fontsize=14)
    fig.suptitle('Petrophysical Logs', fontsize=16)
    plt.tight_layout()


def temp_1(fig,
           df_log,
           perm_col,
           phi_col,
           sw_col,
           ref_limits=(None, None)):

    axs = fig.subplots(nrows=1,
                       ncols=3,
                       sharey=True,
                       gridspec_kw={"wspace": 0})

    logs_to_plot = {'green': perm_col, 'blue': phi_col, 'red': sw_col}

    for ax, (color, log) in zip(axs, logs_to_plot.items()):
        ax.plot(df_log[log], df_log.index, color=color)
        ax.set_title(log)
        ax.xaxis.tick_top()

    axs[0].set_ylim(ref_limits[0], ref_limits[1])
    axs[0].invert_yaxis()
    axs[0].set_ylabel("Depth (m)")


def multi_well(data, template):
    fig_all = plt.figure(figsize=(12, 10))
    subfigs = fig_all.subfigures(1, len(data), wspace=2)
    for idx, (well_name, df) in enumerate(data.items()):
        template(subfigs[idx], df, "KLOGH", "PHIF", "SW")
        subfigs[idx].suptitle(well_name)
    st.pyplot(fig_all)
