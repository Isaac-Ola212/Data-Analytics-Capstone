"""Data cleaning utilities."""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Performs basic cleaning on the dataframe."""
    # placeholder for actual cleaning steps
    df = df.dropna()
    return df
