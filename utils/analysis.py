def get_summary(df):
    """Function to summarize the dataframe"""
    summary = {'Column names': df.columns.to_list(),
               'Number of rows': df.shape[0],
               'Number of columns': df.shape[1],
               'Number of missing values': {k: v for k,v in df.isnull().sum().to_dict().items() if v>0},
               'Number of duplicated': df.duplicated().sum(),
               'Statistics': df.describe().drop('count', axis=0)
               }
    return summary

def get_column_info(df, column):
    """Function to get column information"""
    if df[column].dtype in ['int64', 'float64']:
        info = {'Data type': str(df[column].dtype),
                'Unique values': int(df[column].nunique()),
                'Most frequent values': df[column].value_counts().head().to_dict(),
                'Mean': round(df[column].mean(),2),
                'Median': round(df[column].median(),2),
                'Mode': int(df[column].mode()[0])
                }
    else:
        info = {'Data type': str(df[column].dtype),
                'Unique values': str(df[column].nunique()),
                'Most frequent values': df[column].value_counts().head().to_dict(),
                }
    return info