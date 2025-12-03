import pandas as pd
from pandas.api.types import is_numeric_dtype

class DataCleaner:
    def __init__(self, standard_columns=None):
        self.standard_columns = standard_columns

    def standardize_columns(self, df: pd.DataFrame):
        if self.standard_columns:
            df = df.rename(columns=self.standard_columns)
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
        return df

    def clean_missing(self, df: pd.DataFrame):
        # Basic strategy: drop completely empty rows + fill numeric/string values
        df = df.dropna(how="all")
        df = df.fillna({
            col: df[col].median() if is_numeric_dtype(df[col])  else "Unknown"
            for col in df.columns
        })
        return df

    def clean(self, df: pd.DataFrame):
        df = self.standardize_columns(df)
        df = self.clean_missing(df)
        return df