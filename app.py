import streamlit as st
from ui import render_analysis
from utils.loader import load_csv

st.set_page_config(layout="wide")

st.title("CSV Analyzer") # Title

demo, user = st.tabs(["Demonstration", "Try it yourself"])

with demo: # DEMO
    df = None
    try:
        df = load_csv("data/clients_purchases.csv")
    except Exception as e:
        st.error(f"ERROR! {e}")
    if df is not None:
        render_analysis(df, key_prefix="demo")

with user: # USER
    st.header("Try it yourself")

    st.text("If you want to try it, your file must be a CSV with headers and contain the next ones: age, category, region, total_purchase, purchase_date and quantity.")

    uploaded_file = st.file_uploader("Upload your CSV file here.", type="csv")
    if uploaded_file is not None:
        st.success("Successfully uploaded your CSV file!")
        try:
            df = load_csv(uploaded_file)
        except Exception as e:
            st.error(f"ERROR! {e}")
            st.stop()

        render_analysis(df, key_prefix="user")