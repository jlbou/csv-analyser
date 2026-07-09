import streamlit as st
from utils.analysis import get_summary, get_column_info
from utils.charts import plot_category_sales, plot_sales_by_region, plot_sales_over_time, plot_age_distribution

def render_analysis (df, key_prefix = ""):
    """Function to render the analysis"""

    summary = get_summary(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", summary['Number of rows'])
    col2.metric("Columns", summary['Number of columns'])
    col3.metric("Duplicates", summary['Number of duplicated'])

    st.subheader("Statistics")
    st.dataframe(summary['Statistics'])

    st.subheader("Column information")
    column = st.selectbox("Select a column", df.columns, key=f"{key_prefix}_column_select")
    st.write(get_column_info(df, column))

    st.subheader("Missing values")
    st.dataframe(summary['Number of missing values'])

    if all(col in df.columns for col in ['category', 'total_purchase', 'quantity']):
        st.pyplot(plot_category_sales(df), width=750)
    else:
        st.warning("Columns 'category', 'total_purchase' or 'quantity' are missing")

    if 'age' in df.columns:
        st.pyplot(plot_age_distribution(df), width=750)
    else:
        st.warning("Column 'age' is missing")

    if all(col in df.columns for col in ['purchase_date', 'total_purchase', 'quantity']):
        st.pyplot(plot_sales_over_time(df), width=750)
    else:
        st.warning("Columns 'purchase_date', 'total_purchase' or 'quantity' are missing")

    if all(col in df.columns for col in ['region', 'total_purchase']):
        st.pyplot(plot_sales_by_region(df), width=750)
    else:
        st.warning("Columns 'region' or 'total_purchase' are missing")