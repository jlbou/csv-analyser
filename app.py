import streamlit as st
from utils.loader import load_csv
from utils.analysis import get_summary, get_column_info
from utils.charts import plot_category_sales, plot_sales_by_region, plot_sales_over_time, plot_age_distribution

st.set_page_config(layout="wide")

st.title("CSV Analyzer") # Title

demo, user = st.tabs(["Demonstration", "Try it yourself"])

with demo: # DEMO
    df = load_csv('data/clients_purchases.csv')

    summary = get_summary(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", summary['Number of rows'])
    col2.metric("Columns", summary['Number of columns'])
    col3.metric("Duplicates", summary['Number of duplicated'])

    st.subheader("Statistics")
    st.dataframe(summary['Statistics'])

    st.subheader("Column information")
    column = st.selectbox("Select a column", df.columns)
    st.write(get_column_info(df, column))

    st.subheader("Missing values")
    st.dataframe(summary['Number of missing values'])

    st.pyplot(plot_sales_by_region(df))
    st.pyplot(plot_sales_over_time(df))
    st.pyplot(plot_age_distribution(df))
    st.pyplot(plot_category_sales(df))

with user: # USER
    st.header("Try it yourself")

    uploaded_file = st.file_uploader("Upload your CSV", type="csv")
    if uploaded_file is not None:
        st.success("Successfully uploaded your CSV!")
        df_user = load_csv(uploaded_file)

        summary = get_summary(df_user)

        col1, col2, col3 = st.columns(3)
        col1.metric("Rows", summary['Number of rows'])
        col2.metric("Columns", summary['Number of columns'])
        col3.metric("Duplicates", summary['Number of duplicated'])

        st.subheader("Statistics")
        st.dataframe(summary['Statistics'])

        st.subheader("Missing values")
        st.dataframe(summary['Number of missing values'])

        if all(col in df_user.columns for col in ['category','total_purchase','quantity']):
            st.pyplot(plot_category_sales(df_user))
        else:
            st.warning("Columns 'category', 'total_purchase' or 'quantity' are missing")

        if 'age' in df_user.columns:
            st.pyplot(plot_age_distribution(df_user))
        else:
            st.warning("Column 'age' is missing")

        if all(col in df_user.columns for col in ['purchase_date','total_purchase','quantity']):
            st.pyplot(plot_sales_over_time(df_user))
        else:
            st.warning("Columns 'purchase_date', 'total_purchase' or 'quantity' are missing")

        if all(col in df_user.columns for col in ['region','total_purchase']):
            st.pyplot(plot_sales_by_region(df_user))
        else:
            st.warning("Columns 'region' or 'total_purchases' are missing")