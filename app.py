## Q&A chatbot
from dotenv import load_dotenv

from langchain_community.llms import OpenAI

load_dotenv() ##load envirnomental varibale from .env

import streamlit as st
import os


##funcion to load openai model and get response  

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.5, model_name="gpt-3.5-turbo-instruct")
    response =llm(question)
    return response

##initialize the streamlit application

st.set_page_config(page_title="Q&A demo")

st.header("langchain application")

input =st.text_input("input :",key="input")
response=get_openai_response(input)


submit= st.button("Ask the question")

if submit:
    st.subheader("The response is ")
    st.write(response)