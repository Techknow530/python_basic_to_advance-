import streamlit as st 
import pandas as pd 
import plotly.express as px
import json
import os 

st.set_page_config(page_title="simple Finace app" , page_icon="💰",layout="wide")


def load_transations(file):
    pass
def main():
    st.title("Simple Finance Dashboard ")

    uploaded_file = st.file_uploader("upload Your Transaction csv file " ,type=["csv"])

    if uploaded_file is not None:
        df = load_transations(uploaded_file)


main()