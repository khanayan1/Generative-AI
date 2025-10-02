from dotenv import load_dotenv
load_dotenv()

import streamlit as st
#mport os 
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyBetOKPipyaY6b5Etj774zu38IFtkdB7aY"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")

def get_gemini_response(question):
    response =  model.generate_content(question)
    return response.text

st.set_page_config(page_title="Demo")

st.header("Gemini Application")

question = st.text_input("Enter your question:", key="inpur")

submit = st.button("Submit")

## When submit is click 

if submit:
    response = get_gemini_response(question)
    st.subheader(" The Response is :")
    st.write(response)


