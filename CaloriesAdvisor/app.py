import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_respone(input_prompt,image):
    model=genai.GenerativeModel(model_name="models/gemini-pro-vision")
    respose=model.generate_content([input_prompt,image[0]])
    return respose.text

def input_image_config(uploaded_file):
    if uploaded_file is not None:
        #read the file to bytes
        byte_data=uploaded_file.getvalue()
        image_parts=[
        {
            "mime_type": uploaded_file.type,
            "data": byte_data
        }]
        return image_parts
    else:
        raise FileNotFoundError('no file is uploaded')
    
st.set_page_config(page_title="Gemini health app")
st.header("gemini health app")
uploaded_file = st.file_uploader("upload the image...",type=["jpeg","png","jpg"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="The uploaded image",use_column_width=True)

submit=st.button("tell me about total calories")
input_prompt="""
You are expert in nutritionist where to identify each food item in image and calculate the calories of each food item also provide detailed information list about calories intake
in the below format:
        item_1 = no of calories
        item_2 =no of calories
        -------
        -------
calculate also the total calories of each each food item in image and tell if the meal is healthy or not, provide few some alternative to the food items 
in image, provide the information about the percentage of carbohydrate,protein,fiber,fat present in the image."""

if submit:
    image_data=input_image_config(uploaded_file)
    respose=generate_respone(input_prompt,image_data)
    st.write(respose)





