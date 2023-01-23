# Import python libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import welly
import lasio
from streamlit_option_menu import option_menu
from PIL import Image
from io import StringIO

# Insert icon of web app
icon = Image.open("resources/logs.png")
# Page Layout
st.set_page_config(page_title="Well Logs App", page_icon=icon)

# Title of app
st.title("Well Logs Visualization")
st.write("This logs contain information about petrophysical features of any well")

# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data Information", "Logs Visualization"],
        icons=["house", "clipboard-data", "tv"],
    )

# Options
if options == "Data Information":
    # number of files to upload
    n_wells = int(st.number_input("Enter the well logs files"))
    files = [
        st.file_uploader(f"Upload the las file of well {n + 1}") for n in range(n_wells)
    ]

    if files is not None:
        stringio = [StringIO(log.getvalue().decode("utf-8")) for log in files]
        well_logs = [st.write(lasio.read(log).df()) for log in stringio]

elif options == "Logs Visualization":
    # number of files to upload
    n_wells = int(st.number_input("Enter the well logs files"))
    files = [
        st.file_uploader(f"Upload the las file of well {n + 1}") for n in range(n_wells)
    ]
    if files is not None:
        stringio = [StringIO(log.getvalue().decode("utf-8")) for log in files]
        las_data = [lasio.read(data) for data in stringio]
        well_logs = [log.df() for log in las_data]
        logs = {f"{data.well.keys()}": df for data in las_data for df in well_logs}
