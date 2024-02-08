# CLIP All in one app
This repository contains a streamlit application that demonstrates how to use OpenAI's CLIP model for a variety of natural language and computer vision tasks such as zero-shot classification, image clustering, text clustering, and semantic search.

Deployed App: https://clip-all-in-one.streamlit.app/

- [x]  Zero-shot classification
- [ ]  Image Clustering
- [ ]  Text Clustering   
- [ ]  Semantic Search

# Installation
Clone this repository
```bash
git clone https://github.com/kitsamho/clip_app
```
Install the required packages
```bash
pip install -r requirements.txt
```
Note - This app was made using python 3.9.18
<hr>

# Use
Navigate to the cloned directory and launch the Streamlit app with

```bash
streamlit run clip_app.py
```
Use the sidebar navigation menu to choose the task that you would like to explore.

<hr>

## Repo. structure
```bash
.
├── assets
│ ├── logo.png
│ ├── logo.png
│ ├── logo.png
│ └── logo.png
├── backend
│ ├── init.py
│ ├── clip_functions.py
│ ├── config.yaml
│ ├── dataframes.py
│ ├── load.py
│ ├── pipeline_img_cls.py
│ ├── scraping.py
│ └── show.py
├── README.md
└── clip_app.py
```
