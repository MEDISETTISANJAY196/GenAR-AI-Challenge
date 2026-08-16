import pandas as pd
import json
import os

# -----------------------------------------
# 1. LOAD DATASET
# -----------------------------------------

file_path = "data/Bisoprolol_icsr_sample_1068rows (1).xlsx"

df = pd.read_excel(file_path)

# Convert received date
df["receivedate"] = pd.to_datetime(
    df["receivedate"].astype(str),
    format="%Y%m%d",
    errors="coerce"
)

# -----------------------------------------
# 2. CASE-LEVEL DATA
# -----------------------------------------

cases = df.drop_duplicates(subset="safetyreportid").copy()

total_cases = int(cases["safetyreportid"].nunique())

serious_cases = int(
    (cases["serious"].astype(str).str.lower() == "serious").sum()
)

non_serious_cases = int(
    (cases["serious"].astype(str).str.lower() == "not serious").sum()
)

# -----------------------------------------
# 3. SEX DISTRIBUTION
# -----------------------------------------

sex_distribution = (
    cases["patient_patientsex"]
    .fillna("unknown")
    .value_counts()
    .to_dict()
)

sex_distribution = {
    str(key): int(value)
    for key, value in sex_distribution.items()
}

# -----------------------------------------
# 4. COUNTRY DISTRIBUTION
# -----------------------------------------

country_distribution = (
    cases["occurcountry"]
    .fillna("unknown")
    .value_counts()
    .head(10)
    .to_dict()
)

country_distribution = {
    str(key): int(value)
    for key, value in country_distribution.items()
}

# -----------------------------------------
# 5. AGE GROUP ANALYSIS
# -----------------------------------------

age = pd.to_numeric(
    cases["patient_patientonsetage"],
    errors="coerce"
)

def get_age_group(age_value):
    if pd.isna(age_value):
        return "Unknown"
    elif age_value <= 17:
        return "0-17"
    elif age_value <= 29:
        return "18-29"
    elif age_value <= 44:
        return "30-44"
    elif age_value <= 59:
        return "45-59"
    elif age_value <= 74:
        return "60-74"
    else:
        return "75+"

cases["age_group"] = age.apply(get_age_group)

age_distribution = (
    cases["age_group"]
    .value_counts()
    .to_dict()
)

age_distribution = {
    str(key): int(value)
    for key, value in age_distribution.items()
}

# -----------------------------------------
# 6. REACTION ANALYSIS
# -----------------------------------------

reaction_counts = (
    df["patient_reaction_reactionmeddrapt"]
    .dropna()
    .value_counts()
)

top_reactions = reaction_counts.head(10).to_dict()

top_reactions = {
    str(key): int(value)
    for key, value in top_reactions.items()
}

# -----------------------------------------
# 7. REACTION OUTCOMES
# -----------------------------------------

outcomes = (
    df["patient_reaction_reactionoutcome"]
    .fillna("unknown")
    .astype(str)
    .str.split(",")
    .explode()
    .str.strip()
    .replace("", "unknown")
)

outcome_counts = outcomes.value_counts().to_dict()

outcome_counts = {
    str(key): int(value)
    for key, value in outcome_counts.items()
}

# -----------------------------------------
# 8. SERIOUS REACTION ANALYSIS
# -----------------------------------------

serious_case_ids = cases.loc[
    cases["serious"].astype(str).str.lower() == "serious",
    "safetyreportid"
]

serious_reactions = (
    df[
        df["safetyreportid"].isin(serious_case_ids)
    ]["patient_reaction_reactionmeddrapt"]
    .dropna()
    .value_counts()
    .head(10)
    .to_dict()
)

serious_reactions = {
    str(key): int(value)
    for key, value in serious_reactions.items()
}

# -----------------------------------------
# 9. MONTHLY CASE TREND
# -----------------------------------------

monthly_cases_series = (
    cases
    .dropna(subset=["receivedate"])
    .assign(month=lambda x: x["receivedate"].dt.strftime("%Y-%m"))
    .groupby("month")["safetyreportid"]
    .nunique()
)

monthly_cases = {
    str(key): int(value)
    for key, value in monthly_cases_series.items()
}

# -----------------------------------------
# 10. CREATE FINAL ANALYSIS RESULTS
# -----------------------------------------

analysis_results = {
    "dataset_summary": {
        "total_rows": int(len(df)),
        "total_unique_cases": total_cases,
        "reporting_period": {
            "start_date": str(cases["receivedate"].min().date()),
            "end_date": str(cases["receivedate"].max().date())
        }
    },

    "case_analysis": {
        "serious_cases": serious_cases,
        "non_serious_cases": non_serious_cases
    },

    "patient_analysis": {
        "sex_distribution": sex_distribution,
        "age_distribution": age_distribution,
        "country_distribution": country_distribution
    },

    "reaction_analysis": {
        "top_reactions": top_reactions,
        "top_serious_reactions": serious_reactions,
        "outcome_distribution": outcome_counts
    },

    "trend_analysis": {
        "monthly_case_counts": monthly_cases
    }
}

# -----------------------------------------
# 11. SAVE JSON FILE
# -----------------------------------------

os.makedirs("output", exist_ok=True)

output_file = "output/analysis_results.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(
        analysis_results,
        file,
        indent=4,
        ensure_ascii=False
    )

print("\n===================================")
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("===================================")

print(f"\nTotal Unique Cases: {total_cases}")
print(f"Serious Cases: {serious_cases}")
print(f"Non-Serious Cases: {non_serious_cases}")

print("\nTop 5 Reactions:")
for reaction, count in list(top_reactions.items())[:5]:
    print(f"- {reaction}: {count}")

print(f"\nResults saved to: {output_file}")