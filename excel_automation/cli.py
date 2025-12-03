import argparse
from excel_automation.cleaner import DataCleaner
from excel_automation.merger import FileMerger
from excel_automation.reporter import Reporter
import pandas as pd
import os

def run_pipeline():
    parser = argparse.ArgumentParser(description="Excel Automation Suite")
    parser.add_argument("--output", type=str, default="data/output/merged_cleaned.xlsx",help="Output Excel file path")
    args = parser.parse_args()
    
    # Merge
    merger = FileMerger()
    merged_df = merger.merge()

    # Clean
    cleaner = DataCleaner()
    clean_df = cleaner.clean(merged_df)

    # Save merged + cleaned file
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    clean_df.to_excel(args.output, index=False)

    # Reporting
    reporter = Reporter()
    summary_df = reporter.generate_summary(clean_df)
    reporter.add_summary_sheet(args.output, summary_df)

    print(f"Automation completed. Output saved at {args.output}")