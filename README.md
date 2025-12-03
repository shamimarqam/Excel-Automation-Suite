# **Excel Automation Suite**

A Python-based automation tool for **merging**, **cleaning**, and **reporting** on Excel and CSV datasets.

Designed as a realistic business automation workflow showcasing skills in **Pandas**, **OpenPyXL**, and general data processing.

---

## **Features**

### **Data Operations**

- Merge multiple Excel/CSV files into one unified dataset.
- Standardize column names (lowercase, underscores, trimmed).
- Handle missing values automatically (median for numeric, placeholder for text).
- Drop completely empty rows.

### **Reporting**

- Generate a summary report containing:
  - Total rows
  - Total columns
  - Numeric vs. string column counts
- Append the summary as a new sheet to the final Excel file.

### **Automation & Execution**

- One-command CLI workflow.
- Modular code structure (cleaner, merger, reporter).
- Lightweight and dependency-minimal.

---

## **Folder Structure**

```
excel_automation_suite/
│
├── data/
│   ├── input_files/        # Add your Excel/CSV files here
│   └── output/             # Processed files appear here
│
├── excel_automation/
│   ├── cleaner.py
│   ├── merger.py
│   ├── reporter.py
│   ├── cli.py
│   └── __init__.py
│
├── main.py                 # Entry point for the automation pipeline
└── requirements.txt
```

---

## **Installation**

### **1. Clone the repository**

```
git clone https://github.com/yourusername/excel-automation-suite.git
cd excel-automation-suite
```

### **2. Install dependencies**

```
pip install -r requirements.txt
```

---

## **Usage**

### **Step 1: Add your files**

Place all input Excel and CSV files inside:

```
data/input_files/
```

### **Step 2: Run the automation**

```
python main.py --output data/output/merged_cleaned.xlsx
```

### **Step 3: Output**

The tool will generate:

1. **merged_cleaned.xlsx** – merged + cleaned dataset
2. A **Summary_Report** sheet inside the same file

---

## **Example Output (Summary Sheet)**

| **Metric** | **Value** |
| ---------------- | --------------- |
| row_count        | 10234           |
| column_count     | 12              |
| numeric_columns  | 7               |
| string_columns   | 5               |
