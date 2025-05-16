import streamlit as st
from renders import sidebar
import streamlit.components.v1 as components

with st.sidebar:
    sidebar.render()
    

def read_html():
    with open("./core/index.html") as f:
        return f.read()

components.html(
    read_html(),
    height=0,
    width=0,
)
