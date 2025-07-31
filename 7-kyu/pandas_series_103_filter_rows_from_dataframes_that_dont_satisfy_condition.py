import pandas as pd


def filter_dataframe(df, col, func): 
    if col not in df.columns:
        raise ValueError(f"Column '{col}' is not present in the DataFrame.")

    mask = ~df[col].apply(func)
    return df[mask]
