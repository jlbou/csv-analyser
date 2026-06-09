import seaborn as sb
import matplotlib.pyplot as plt

def plot_category_sales(df):
    """Function to plot sales by category"""
    data = df.groupby('category')['total_sales'].sum().reset_index()

    fig, ax = plt.subplots()

    sb.barplot(data=data, x='category', y='total_sales', ax=ax)

    ax.set_title('Sales by category')
    ax.set_xlabel('Category')
    ax.set_ylabel('Total Sales')

    return fig