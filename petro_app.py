# Import python libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import welly
import lasio
from streamlit_option_menu import option_menu
from PIL import Image
from pathlib import Path

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
    # number of file to upload
    n_wells = int(st.number_input("Enter the well logs files"))
    files = [
        st.file_uploader(f"Upload the las file of well {n + 1}") for n in range(n_wells)
    ]

elif options == "Logs Visualization":
