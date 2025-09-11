import pandas as pd

def rename_columns(df, names):
    temp = df.copy()
    temp.columns = names
    return temp
