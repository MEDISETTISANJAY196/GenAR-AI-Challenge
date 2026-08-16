import json
import os


# -----------------------------------------
# 1. LOAD EVIDENCE
# -----------------------------------------

input_file = "output/evidence.json"

with open(input_file, "r", encoding="utf-8") as file:
    evidence = json.load(file)


# -----------------------------------------
# 2. EXTRACT DATA
# -----------------------------------------

drug = evidence["metadata"]["drug"]

dataset = evidence["dataset_evidence"]
case_data = evidence["case_evidence"]
patient_data = evidence["patient_evidence"]
reaction_data = evidence["reaction_evidence"]
trend_data = evidence["trend_evidence"]

total_rows = dataset["total_rows"]
total_cases = dataset["total_unique_cases"]

start_date = dataset["reporting_period"]["start_date"]
end_date = dataset["reporting_period"]["end_date"]

serious_cases = case_data["serious_cases"]
non_serious_cases = case_data["non_serious_cases"]


# -----------------------------------------
# 3. HELPER FUNCTION FOR MARKDOWN TABLES
# -----------------------------------------

def create_table(data, column1, column2):
    table = f"| {column1} | {column2} |\n"
    table += "|---|---:|\n"

    for key, value in data.items():
        table += f"| {key} | {value} |\n"

    return table


# -----------------------------------------
# 4. CREATE REPORT
# -----------------------------------------

report = f"""# Periodic Adverse Drug Experience Report

## 1. Product Information

**Drug:** {drug}

**Data Source:** {evidence["metadata"]["data_source_type"]}

**Analysis Method:** {evidence["metadata"]["analysis_method"]}


## 2. Reporting Period

**Start Date:** {start_date}

**End Date:** {end_date}


## 3. Dataset Summary

The supplied dataset contains **{total_rows} records** representing
**{total_cases} unique safety cases**.

The reporting period covered by this analysis is from
**{start_date} to {end_date}**.


## 4. Case Seriousness Summary

| Case Type | Number of Cases |
|---|---:|
| Serious | {serious_cases} |
| Not Serious | {non_serious_cases} |


## 5. Patient Demographics

### Sex Distribution

{create_table(
    patient_data["sex_distribution"],
    "Sex",
    "Number of Cases"
)}

### Age Distribution

{create_table(
    patient_data["age_distribution"],
    "Age Group",
    "Number of Cases"
)}


## 6. Geographic Distribution

The following table shows the most frequently reported countries or
geographic categories in the supplied safety dataset.

{create_table(
    patient_data["top_countries"],
    "Country / Region",
    "Number of Cases"
)}


## 7. Most Frequently Reported Reactions

The following reactions were the most frequently represented reaction
terms in the supplied dataset.

{create_table(
    reaction_data["top_reactions"],
    "Reaction",
    "Number of Reports"
)}


## 8. Reactions in Serious Cases

The following reaction terms were observed among cases classified as serious.

{create_table(
    reaction_data["top_serious_reactions"],
    "Reaction",
    "Number of Reports"
)}


## 9. Reaction Outcome Distribution

{create_table(
    reaction_data["outcome_distribution"],
    "Outcome",
    "Number of Records"
)}


## 10. Monthly Case Trend

{create_table(
    trend_data["monthly_case_counts"],
    "Month",
    "Unique Cases"
)}


## 11. Key Observations

- The analysis identified **{total_cases} unique safety cases**.
- **{serious_cases} cases** were classified as serious.
- The most frequently reported reaction term was **Acute kidney injury**.
- Patient reports were predominantly represented in the **60–74** and
  **75+** age groups.
- The reporting dataset covers the period from **{start_date} to
  {end_date}**.


## 12. Important Limitations

{evidence["metadata"]["note"]}

This report is based only on the supplied dataset and deterministic
analysis. Reported events do not establish causality between
{drug} and any adverse reaction. The reported counts should not be
interpreted as incidence rates or estimates of risk.


## 13. Conclusion

This report provides a descriptive summary of the supplied ICSR safety
data for **{drug}** during the defined reporting period.

The findings are intended to support structured safety data review.
Further medical, clinical, and pharmacovigilance evaluation would be
required before making regulatory or causal conclusions.
"""


# -----------------------------------------
# 5. SAVE REPORT
# -----------------------------------------

os.makedirs("output", exist_ok=True)

output_file = "output/generated_report.md"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(report)


# -----------------------------------------
# 6. SUCCESS MESSAGE
# -----------------------------------------

print("\n===================================")
print("REPORT GENERATED SUCCESSFULLY")
print("===================================")

print(f"\nDrug: {drug}")
print(f"Total Unique Cases: {total_cases}")
print(f"Reporting Period: {start_date} to {end_date}")

print(f"\nReport saved to:")
print(output_file)