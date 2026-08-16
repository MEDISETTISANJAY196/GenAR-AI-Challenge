import json
import os


# -----------------------------------------
# 1. LOAD ANALYSIS RESULTS
# -----------------------------------------

input_file = "output/analysis_results.json"

with open(input_file, "r", encoding="utf-8") as file:
    analysis = json.load(file)


# -----------------------------------------
# 2. EXTRACT IMPORTANT EVIDENCE
# -----------------------------------------

evidence = {
    "dataset_evidence": {
        "total_rows": analysis["dataset_summary"]["total_rows"],
        "total_unique_cases": analysis["dataset_summary"]["total_unique_cases"],
        "reporting_period": analysis["dataset_summary"]["reporting_period"]
    },

    "case_evidence": {
        "serious_cases": analysis["case_analysis"]["serious_cases"],
        "non_serious_cases": analysis["case_analysis"]["non_serious_cases"]
    },

    "patient_evidence": {
        "sex_distribution": analysis["patient_analysis"]["sex_distribution"],
        "age_distribution": analysis["patient_analysis"]["age_distribution"],
        "top_countries": analysis["patient_analysis"]["country_distribution"]
    },

    "reaction_evidence": {
        "top_reactions": analysis["reaction_analysis"]["top_reactions"],
        "top_serious_reactions": analysis["reaction_analysis"]["top_serious_reactions"],
        "outcome_distribution": analysis["reaction_analysis"]["outcome_distribution"]
    },

    "trend_evidence": {
        "monthly_case_counts": analysis["trend_analysis"]["monthly_case_counts"]
    }
}


# -----------------------------------------
# 3. ADD EVIDENCE METADATA
# -----------------------------------------

evidence["metadata"] = {
    "drug": "Bisoprolol",
    "data_source_type": "ICSR safety reports",
    "analysis_method": "Deterministic Python and Pandas analysis",
    "note": (
        "This evidence contains descriptive findings from the supplied dataset. "
        "Counts represent reported cases or reaction records and should not be "
        "interpreted as incidence rates or causal conclusions."
    )
}


# -----------------------------------------
# 4. SAVE EVIDENCE
# -----------------------------------------

os.makedirs("output", exist_ok=True)

output_file = "output/evidence.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(
        evidence,
        file,
        indent=4,
        ensure_ascii=False
    )


# -----------------------------------------
# 5. SUCCESS MESSAGE
# -----------------------------------------

print("\n===================================")
print("EVIDENCE BUILT SUCCESSFULLY")
print("===================================")

print(f"\nDrug: {evidence['metadata']['drug']}")
print(
    f"Total Unique Cases: "
    f"{evidence['dataset_evidence']['total_unique_cases']}"
)

print("\nEvidence saved to:")
print(output_file)