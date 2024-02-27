import streamlit as st
from langchain.prompts import PromptTemplate  31    \1
from langchain_community.llms import CTransformers

#function get response from llamma2 model
def get_llama_response(input_txt, no_of_words,blog_style):
    #import llama model
    config = {'max_new_tokens': 256, 'temperature': 0.01}
    llm=CTransformers(model='D:\python\model\Models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config=config,
                      )
    template="""
Create blog for {blog_style} for the topic {input_txt} within
{no_of_words} words."""

    prompt=PromptTemplate(input_variables=["blog_style",'input_txt','no_of_words'],template=template)

    response=llm(prompt.format(blog_style=blog_style,input_txt=input_txt,no_of_words=no_of_words))
    print(response)
    return response




st.set_page_config(
    page_title="Generate blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)
 
st.header('Generate blogs')

input_txt=st.text_input('enter the blog topic')

#additional inputs for blogs
col1, col2 =st.columns([5,5])

with col1:
    no_of_words=st.text_input('number of words')

with col2:
    blog_style=st.selectbox('for whom?',('Researcher','Data scientist','Common people'),index=0)


submit=st.button('click to generate')

if submit:
    st.write(get_llama_response(input_txt,no_of_words,blog_style))