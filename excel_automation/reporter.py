import pandas as pd
from openpyxl import load_workbook

class Reporter:
    def generate_summary(self, df: pd.DataFrame):
        summary = {
            "row_count": len(df),
            "column_count": len(df.columns),
            "numeric_columns": df.select_dtypes(include="number").shape[1],
            "string_columns": df.select_dtypes(include="object").shape[1]
        }
        return pd.DataFrame.from_dict(summary, orient="index", columns=["value"])

    def add_summary_sheet(self, file_path: str, df_summary: pd.DataFrame):
        # Load file and append sheet
        writer = pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace")
        df_summary.to_excel(writer, sheet_name="Summary_Report")
        writer.close()