import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.title("Savor")
st.caption("Savor what you have, and you will have more of it.")
st.write("**Github repository**: https://github.com/SavorApp2023/SavorApp")


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
aps = st.button("Go to app!")
if aps:
    switch_page("main")
st.subheader("The story behind Savor")
st.write(
    "Savor was born out of a desire to reduce food waste and help people make the most out of the ingredients they already have. As a team of food enthusiasts and tech lovers, we recognized that there was a need for a more accessible and user-friendly approach to cooking and meal planning. We wanted to create an app that could take the stress out of meal planning and make cooking easy for everyone. With a simple tap of a button, Savor generates dynamic, delicious recipes based on the ingredients you have on hand, taking into account nutritional value and dietary preferences. Whether you're a beginner cook or a seasoned pro, Savor has something for everyone, and its user-friendly interface makes cooking easy and fun."
)


st.image("number1.png")

col1, col2 = st.columns(2)

with col1:
    st.subheader("What is Savor?")
    st.write(
        "Savor is an innovative solution to the way people approach cooking and food preparation. Its AI-generated recipes allow users to make the most out of the ingredients they already have in their fridge, reducing food waste and making healthy, nutritious meals more accessible and affordable. Frequently, people order takeout from outside or spend a lot of money on excess groceries because they are unsure what to cook with the ingredients they already have at home. Savor solves this problem by providing users with a variety of recipes that are tailored to their specific dietary preferences and nutritional needs, while **only using the ingredients they already have lying in their fridge**. By using Savor, you'll never be at a loss for what to make for dinner again, and you'll be making a positive impact on the world by reducing food waste and helping address the issue of world hunger."
    )
with col2:
    st.image("chef.png")

with col1:
    st.subheader("How it works")
    st.write(
        "Savor prioritizes a simplistic interface. The front-end is powered by Streamlit and is beautiful, responsive, and clean. Users have the option to list the ingredients they have on hand and their dietary restrictions in plain text, or simply upload a photo of their fridge. Savor uses a combination of computer vision through YOLOv5 and natural language processing through OpenAI's powerful gpt-3.5-turbo algorithm to identify the ingredients present in the photo and generate recipes based on the user's preferences."
    )
with col2:
    st.image("Screenshot_26.png")


with col1:
    st.subheader("Inspiration")
    st.write(
        "Our inspiration for Savor came from our own experiences as home cooks. We often found ourselves staring blankly at the contents of our fridges, wondering what to make for dinner. We also recognized the issue of food waste, hunger and how much perfectly good food was being thrown away because people didn't know what to do with it. We wanted to create an app that could help solve both of these problems."
    )


with col2:
    st.image("hunger.jpg")
