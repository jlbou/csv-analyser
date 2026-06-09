import pandas as pd

def load_csv(path):
    """Function to load csv file and return a pandas dataframe"""
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f'File {path} not found')
    except pd.errors.ParserError:
        raise Exception(f'Error while reading file')