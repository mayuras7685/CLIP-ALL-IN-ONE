import requests
from PIL import Image
import plotly.express as px
import altair as alt
import streamlit as st
from backend.load import load_yaml


def open_image(url):
    # Set the URL of a random image to fetch
    image = Image.open(requests.get(url, stream=True).raw)
    return image


def plot_results(df, y_label, x_label, color_discrete_sequence):
    fig = px.bar(df, y=y_label, x=x_label, range_y=[0, 1], height=300, width=400, text=y_label,\
                 color_discrete_sequence=[color_discrete_sequence])
    fig.update_traces(texttemplate='%{text:.0%}', textposition='auto',textfont_size=20) # formats the text on the bar as a percentage
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)', })

    return fig


def tech_summary_side_bar(config_key):
    config = load_yaml("config.yaml")
    expander_info = config['MORE_INFO'][config_key]
    st.sidebar.markdown('#')
    st.sidebar.markdown('#')
    st.sidebar.write(expander_info)
    return