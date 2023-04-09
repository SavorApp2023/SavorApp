import streamlit as st
import pandas as pd
import requests
import urllib.request
from PIL import Image
from io import BytesIO
from google_images_search import GoogleImagesSearch
import requests
from bs4 import BeautifulSoup
import random
import json
import createRecipe
from streamlit_extras.switch_page_button import switch_page
import torch
import plotly.express as px
import numpy as np


def getImage(name):

    gis = GoogleImagesSearch(st.secrets("google"), "c1bf1c2491f384145")
    gis.search({"q": name, "num": 1})
    result = gis.results()[0]
    img_url = result.url
    print(img_url)
    return img_url


def remove_duplicates(lst):
    return list(set(lst))


def list_to_string(lst):
    return " ".join([str(i) for i in lst if str(i).isalnum()])


st.markdown(
    """
        <style>
            [data-testid="stSidebarNav"] {
                background-repeat: no-repeat;                
            }
            [data-testid="stSidebarNav"]::before {
                content: "Savor";
                margin-left: 20px;
                margin-top: 20px;

                font-size: 30px;
                text-align: center;
                position: relative;
            }
        </style>
        """,
    unsafe_allow_html=True,
)


st.title("Savor")
st.caption("Use what you have, and you will have more to savor.")
ings = st.text_input(
    "Input the ingredients that you have avaliable in your fridge! Also input your dietary restrictions, if any exist."
)
if st.button("Generate Recipes"):
    recipes = createRecipe.write_prompt(ings)
    st.subheader("Recipes")
    col1, col2, col3 = st.columns(3)
    with col1:
        fd = recipes["recipes"][0]["name"]
        st.header(fd)
        st.image(getImage(fd), width=200)
    with col2:
        fd = recipes["recipes"][1]["name"]
        st.header(fd)
        st.image(getImage(fd), width=200)
    with col3:
        fd = recipes["recipes"][2]["name"]
        st.header(fd)
        st.image(getImage(fd), width=200)
    with st.expander("Recipe 1"):
        st.subheader(recipes["recipes"][0]["name"])
        st.write("## Ingredients")
        for ing in recipes["recipes"][0]["ingredients"]:
            st.write(f"- {ing['name']}: {ing['quantity']}")
        st.write("## Steps")
        for i, step in enumerate(recipes["recipes"][0]["steps"]):
            st.write(f"{i+1}. {step}")
    with st.expander("Recipe 2"):
        st.subheader(recipes["recipes"][1]["name"])
        st.write("## Ingredients")
        for ing in recipes["recipes"][1]["ingredients"]:
            st.write(f"- {ing['name']}: {ing['quantity']}")
        st.write("## Steps")
        for i, step in enumerate(recipes["recipes"][1]["steps"]):
            st.write(f"{i+1}. {step}")
    with st.expander("Recipe 3"):
        st.subheader(recipes["recipes"][2]["name"])
        st.write("## Ingredients")
        for ing in recipes["recipes"][2]["ingredients"]:
            st.write(f"- {ing['name']}: {ing['quantity']}")
        st.write("## Steps")
        for i, step in enumerate(recipes["recipes"][2]["steps"]):
            st.write(f"{i+1}. {step}")


image = st.file_uploader(
    "Upload an Image of your fridge (Experimental)",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=False,
)

if image:
    try:
        image = Image.open(image)
        model = torch.hub.load("ultralytics/yolov5", "custom", "yolov5l.pt")
        results = model(image, size=640)
        fig = px.imshow(np.squeeze(results.render()), aspect="equal")

        # st.text(results.pandas().xyxy)
        name = results.pandas().xyxy[0]["name"].tolist()
        name = remove_duplicates(name)
        st.text(name)
        confidence = round(
            (results.pandas().xyxy[0]["confidence"].unique()[0] * 100), 2
        )
        name = list_to_string(name)
        recipes = createRecipe.write_prompt(name)
        st.subheader("Recipes")
        col1, col2, col3 = st.columns(3)
        with col1:
            fd = recipes["recipes"][0]["name"]
            st.header(fd)
            st.image(getImage(fd), width=200)
        with col2:
            fd = recipes["recipes"][1]["name"]
            st.header(fd)
            st.image(getImage(fd), width=200)
        with col3:
            fd = recipes["recipes"][2]["name"]
            st.header(fd)
            st.image(getImage(fd), width=200)
        with st.expander("Recipe 1"):
            st.subheader(recipes["recipes"][0]["name"])
            st.write("## Ingredients")
            for ing in recipes["recipes"][0]["ingredients"]:
                st.write(f"- {ing['name']}: {ing['quantity']}")
            st.write("## Steps")
            for i, step in enumerate(recipes["recipes"][0]["steps"]):
                st.write(f"{i+1}. {step}")
        with st.expander("Recipe 2"):
            st.subheader(recipes["recipes"][1]["name"])
            st.write("## Ingredients")
            for ing in recipes["recipes"][1]["ingredients"]:
                st.write(f"- {ing['name']}: {ing['quantity']}")
            st.write("## Steps")
            for i, step in enumerate(recipes["recipes"][1]["steps"]):
                st.write(f"{i+1}. {step}")
        with st.expander("Recipe 3"):
            st.subheader(recipes["recipes"][2]["name"])
            st.write("## Ingredients")
            for ing in recipes["recipes"][2]["ingredients"]:
                st.write(f"- {ing['name']}: {ing['quantity']}")
            st.write("## Steps")
            for i, step in enumerate(recipes["recipes"][2]["steps"]):
                st.write(f"{i+1}. {step}")
    except Exception as e:
        print(e)
        st.text("No food detected.")
