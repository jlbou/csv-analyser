import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

def plot_category_sales(df):
    """Function to plot sales by category"""
    data = df.groupby('category')[['total_purchase', 'quantity']].sum().reset_index()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    sb.barplot(data=data, x='category', y='total_purchase', ax=ax1)
    sb.barplot(data=data, x='category', y='quantity', ax=ax2)

    ax1.set_title('Sales by category')
    ax1.set_xlabel('Category')
    ax1.set_ylabel('Total Sales')
    ax2.set_title('Quantity by category')
    ax2.set_xlabel('Category')
    ax2.set_ylabel('Quantity')

    plt.tight_layout()

    return fig

def plot_age_distribution(df):
    """Function to plot age distribution"""
    fig, ax = plt.subplots()

    sb.histplot(data=df, x='age', bins=10, ax=ax)

    ax.set_title('Age distribution')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')

    return fig

def plot_sales_over_time(df):
    """Function to plot sales over time"""

    df['purchase_date'] = pd.to_datetime(df['purchase_date'])
    df['month'] = df['purchase_date'].dt.to_period('M')
    df['month'] = df['month'].astype(str)
    data = df.groupby('month')[['total_purchase', 'quantity']].sum().reset_index()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    sb.lineplot(data=data, x='month', y='total_purchase', ax=ax1)
    sb.lineplot(data=data, x='month', y='quantity', ax=ax2)

    ax1.set_title('Sales over time')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Total Sales')
    ax1.tick_params(axis='x', rotation=45)

    ax2.set_title('Quantity over time')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Quantity')
    ax2.tick_params(axis='x', rotation=45)

    plt.tight_layout()

    return fig

def plot_sales_by_region(df):
    """Function to plot sales by region"""
    data = df.groupby('region')['total_purchase'].sum().reset_index()

    fig, ax = plt.subplots()

    sb.barplot(data=data, x='region', y='total_purchase', ax=ax)

    ax.set_title('Sales by region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Sales')
    ax.tick_params(axis='x', rotation=90)

    return fig