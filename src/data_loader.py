import pandas as pd

# Dataset file path
file_path = "data/Bisoprolol_icsr_sample_1068rows (1).xlsx"

# Load dataset
df = pd.read_excel(file_path)

print("\n--- BASIC DATASET CHECK ---")

# Total rows
print(f"Total Rows: {len(df)}")

# Unique safety cases
print(f"Unique Safety Cases: {df['safetyreportid'].nunique()}")

# Serious / Non-serious
print("\n--- SERIOUSNESS ---")
print(df["serious"].value_counts(dropna=False))

# Patient Sex
print("\n--- PATIENT SEX ---")
print(df["patient_patientsex"].value_counts(dropna=False))

# Top 10 Reactions
print("\n--- TOP 10 REACTIONS ---")
print(
    df["patient_reaction_reactionmeddrapt"]
    .value_counts()
    .head(10)
)

# Received Date Range
print("\n--- RECEIVED DATE RANGE ---")

df["receivedate"] = pd.to_datetime(
    df["receivedate"].astype(str),
    format="%Y%m%d",
    errors="coerce"
)

print(f"Start Date: {df['receivedate'].min()}")
print(f"End Date: {df['receivedate'].max()}")