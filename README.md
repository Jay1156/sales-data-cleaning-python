# Sales Data Cleaning with Python (Pandas)

## Overview
In this project, I took a raw B2B sales dataset (`sales_data_sample.csv`) with 2,823 rows and 25 columns and cleaned it step-by-step using Python and Pandas. The main goal was to fix real-world data issues—like encoding glitches, missing values, inconsistent state codes, and messy spacing—so the final file (`sales_data_cleaned.csv`) is actually ready for SQL querying, EDA, or Tableau dashboards without breaking anything downstream.

## Project Structure
```
sales-data-cleaning-python/
├── data/
│   ├── raw/
│   │   └── sales_data_sample.csv
│   └── processed/
│       └── sales_data_cleaned.csv
├── scripts/
│   └── pandasProject.py
└── README.md
```

## What I Fixed in the Data
1. **Preserved North America (`"NA"`) in `territory`:** By default, Pandas treats `"NA"` as a missing value (`NaN`). I handled this properly so North American region records stayed intact instead of showing up as nulls.
2. **Standardized `state` & `postalcode`:** Converted postal codes cleanly to strings and stripped extra spaces. Also mapped 10 abbreviated international state codes (across US, Canada, and Australia) to their full names and filled remaining missing states with `"Unknown"`.
3. **Fixed Broken Encoding (Mojibake) Text:** Found corrupted characters (`Ã...`) in a few customer addresses and names (`Berguvsvägen 8`, `Rambla de Cataluña, 23`, and `Martín`) caused by encoding mismatches, and cleaned them up using targeted string replacements.
4. **Whitespace & Column Cleanup:** Trimmed leading and trailing spaces from contact names and deal sizes, and reordered `contactfirstname` before `contactlastname` so customer names read naturally left-to-right.
5. **Final Sanity Checks:** Verified there are zero duplicate rows, zero unintended nulls, and exact column counts (2,823 rows × 25 columns) before exporting.

## Tools Used
- Python 3
- Pandas

## How to Run It
1. Clone this repository to your local machine: `git clone https://github.com/Jay1156/sales-data-cleaning-python.git`
2. Open your terminal inside the project root folder, make sure Pandas is installed (`pip install pandas`), and run `python scripts/pandasProject.py`

## What's Next
Now that the dataset is clean, I'm planning to use `data/processed/sales_data_cleaned.csv` for exploratory data analysis (EDA) and build a sales performance dashboard on top of it.