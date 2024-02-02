import streamlit as st
from backend.clip_functions import download_clip_model


st.set_page_config(layout="wide")

config = load_yaml("config.yaml")
clip_model = config['CLIP_MODEL'][0]

model, processor, tokenizer = download_clip_model(clip_model) #load the model

