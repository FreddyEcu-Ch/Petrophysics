# Import python libraries
import streamlit as st
import pandas as pd
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

