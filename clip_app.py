import pandas as pd
import streamlit as st
from backend.app_pages import image_classification, text_classification, image_clustering, semantic_searh
from backend.clip_functions import download_clip_model
from backend.load import load_yaml
from backend.app_pages import data


st.set_page_config(layout="wide")

@st.cache_data
def load_cached_embeddings(path: str):
    df = pd.read_pickle(path)
    return df

config = load_yaml("config.yaml")
clip_model = config['CLIP_MODEL'][0]
model, processor, tokeniser = download_clip_model(clip_model) # load the model, processor and tokeniser - this is cached

# Define menu items for each sub-app
# Define menu items for each sub-app
navigation_buttons = {"Zero Shot Image Classification": image_classification,
                      "Zero Shot Text Classification": text_classification,
                      "Image Clustering": image_clustering,
                      "Semantic Search": semantic_searh,
}

st.sidebar.title('CLIP Demo')
selection = st.sidebar.radio("Go to", list(navigation_buttons.keys()))
page = navigation_buttons[selection]
if selection == 'Zero Shot Image Classification':
    page.write(processor, model, tokeniser)

elif selection == 'Zero Shot Text Classification':
    page.write(tokeniser, model)

elif selection == 'Image Clustering':
    page.write(df_cached_embeddings_rock, processor, model)

elif selection == 'Semantic Search':
    page.write(df_cached_embeddings_rock, model, tokeniser)