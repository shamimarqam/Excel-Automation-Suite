import os
import pandas as pd

class FileMerger:
    def __init__(self, input_path="data/input_files/"):
        self.input_path = input_path

    def load_files(self):
        dfs = []
        for file in os.listdir(self.input_path):
            full_path = os.path.join(self.input_path, file)
            if file.endswith(".xlsx") or file.endswith(".xls"):
                dfs.append(pd.read_excel(full_path))
            elif file.endswith(".csv"):
                dfs.append(pd.read_csv(full_path))
        return dfs

    def merge(self):
        dfs = self.load_files()
        if not dfs:
            raise ValueError("No Excel or CSV files found in input_files/")
        merged = pd.concat(dfs, ignore_index=True)
        return merged