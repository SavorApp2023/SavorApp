import openai
import streamlit as st
import json

openai.api_key = st.secrets("openai")


def ask_gpt(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": 'You are a robot who suggest 3 different recipes that uses these following ingredients and implements the given dietary restrictions, feel free to add other recipes. Please provide the recipes in JSON format, with them in list format enclosed within an external dictionary key called "recipes", with a name string, an ingredients list, and make sure to have recipe steps. Each ingredient should be represented by a dictionary with a name and quantity, and the recipe steps should be represented as an array of strings. Make sure your response is valid json with no other text and no markup. ONLY JSON and MAKE SURE TO FOLLOW STRUCTURE! NO MARKUP including ```!. Only incorporate the dietary restrictions in your recipe selections and choices, do not mention it anywhere including in the JSON.',
            },
            {"role": "user", "content": prompt +
                " remember no text other than json"},
        ],
    )

    answer = completion["choices"][0]["message"]["content"]
    print(answer)
    return answer


def write_prompt(ingredients):
    prompt = f"I have {ingredients}. "

    return json.loads(ask_gpt(prompt))
