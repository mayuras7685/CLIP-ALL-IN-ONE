import yaml
import streamlit as st
import random

@st.cache_data
def load_yaml(filename):
  with open('backend/'+filename, 'r') as config_file:
    yml_file = yaml.load(config_file, Loader=yaml.FullLoader)
  return yml_file

