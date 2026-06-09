def get_summary(df):
    '''Function to summarize the dataframe'''
    summary = {'Column names': df.columns.to_list(),'Number of rows': df.shape[0], 'Number of columns': df.shape[1],
               'Number of missing values': df.isnull().sum().to_dict(), 'Number of duplicated': df.duplicated().sum(),
               'Statistics': df.describe()}
    return summary

def get_column_info(df, column):
    '''Function to get column information'''
    if df[column].dtype in ['int64', 'float64']:
        info = {'Data type': df[column].dtype,
                'Unique values': df[column].nunique(),
                'Most frequent values': df[column].value_counts().head(),
                'Mean': df[column].mean(),
                'Median': df[column].median(),
                'Mode': df[column].mode()[0],}
    else:
        info = {'Data type': df[column].dtype,
                'Unique values': df[column].nunique(),
                'Most frequent values': df[column].value_counts().head()}
    return info