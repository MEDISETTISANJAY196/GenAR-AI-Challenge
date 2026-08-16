import pandas as pd
import sys
import os


print("\n" + "=" * 50)
print("DATA VALIDATION")
print("=" * 50)


# Dataset path
DATA_PATH = "data/Bisoprolol_icsr_sample_1068rows (1).xlsx"


# Check file exists
if not os.path.exists(DATA_PATH):
    print(f"\nERROR: Dataset file not found!")
    print(f"Expected path: {DATA_PATH}")
    sys.exit(1)


# Load dataset
try:
    df = pd.read_excel(DATA_PATH)
    print("\n✓ Dataset loaded successfully")
except Exception as e:
    print(f"\nERROR: Could not load dataset")
    print(e)
    sys.exit(1)


# Required columns
required_columns = [
    "safetyreportid",
    "serious",
    "patient_patientsex",
    "patient_patientonsetage",
    "occurcountry",
    "patient_reaction_reactionmeddrapt",
    "receivedate"
]


print("\n--- REQUIRED COLUMN CHECK ---")

missing_columns = []

for column in required_columns:
    if column in df.columns:
        print(f"✓ {column}")
    else:
        print(f"✗ {column} - MISSING")
        missing_columns.append(column)


if missing_columns:
    print("\nValidation Failed!")
    print("Missing required columns:")
    for column in missing_columns:
        print(f"- {column}")
    sys.exit(1)


# Basic dataset information
print("\n--- DATASET SUMMARY ---")

print(f"Total Rows: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print(f"Unique Safety Cases: {df['safetyreportid'].nunique()}")


# Missing values
print("\n--- MISSING VALUES CHECK ---")

for column in required_columns:

    missing_count = df[column].isna().sum()
    missing_percent = (missing_count / len(df)) * 100

    print(
        f"{column}: "
        f"{missing_count} missing "
        f"({missing_percent:.2f}%)"
    )


# Duplicate row check
duplicate_rows = df.duplicated().sum()

print("\n--- DUPLICATE CHECK ---")
print(f"Exact Duplicate Rows: {duplicate_rows}")


# Duplicate case IDs
duplicate_case_rows = df["safetyreportid"].duplicated().sum()

print(
    f"Repeated Safety Report IDs: "
    f"{duplicate_case_rows}"
)


# Date validation
print("\n--- DATE VALIDATION ---")

df["receivedate_parsed"] = pd.to_datetime(
    df["receivedate"],
    format="%Y%m%d",
    errors="coerce"
)

invalid_dates = df["receivedate_parsed"].isna().sum()

print(f"Invalid / Missing Dates: {invalid_dates}")

valid_dates = df["receivedate_parsed"].dropna()

if len(valid_dates) > 0:
    print(f"Start Date: {valid_dates.min().date()}")
    print(f"End Date: {valid_dates.max().date()}")


# Final result
print("\n" + "=" * 50)

if len(missing_columns) == 0:
    print("VALIDATION COMPLETED SUCCESSFULLY")
    print("=" * 50)
    print("\nDataset is ready for analysis.")
else:
    print("VALIDATION FAILED")

print("=" * 50)