# CLIP All in one app
This repository contains a streamlit application that demonstrates how to use OpenAI's CLIP model for a variety of natural language and computer vision tasks such as zero-shot classification, image clustering, text clustering, and semantic search.

Deployed App: https://clip-all-in-one.streamlit.app/

- [x]  Zero-shot image classification
- [x]  Zero-shot text classification
- [x]  Semantic Search
- [x]  Image Clustering
- [ ]  Text Clustering   


# Installation
Get the Access Key from the unsplash
- Visit the [Unsplash-Developer](https://unsplash.com/developers)
- Register your app and get the Access Key
- Create .env file (For eg. see the dotenv file in the repo)

- .env should look like
```bash
ACCESS_KEY="<your key>"
```

Clone this repository
```bash
git clone https://github.com/mayuras7685/CLIP-ALL-IN-ONE
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
