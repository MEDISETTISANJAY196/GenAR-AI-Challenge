import json


def generate_safety_narrative(evidence):
    """
    Generate a controlled safety narrative from
    the trusted evidence layer.

    This module does not calculate statistics.
    All numerical values come from evidence.json.
    """

    dataset = evidence["dataset_evidence"]
    case_data = evidence["case_evidence"]
    patient_data = evidence["patient_evidence"]
    reaction_data = evidence["reaction_evidence"]

    total_cases = dataset["total_unique_cases"]
    serious_cases = case_data["serious_cases"]
    non_serious_cases = case_data["non_serious_cases"]

    top_reactions = reaction_data["top_reactions"]

    top_reaction = list(top_reactions.keys())[0]
    top_reaction_count = top_reactions[top_reaction]

    age_distribution = patient_data["age_distribution"]

    narrative = f"""
## AI-Generated Safety Narrative

Based on the approved evidence generated from the supplied ICSR dataset,
the analysis identified {total_cases} unique safety cases.

Of these cases, {serious_cases} were classified as serious and
{non_serious_cases} were classified as non-serious.

The most frequently reported reaction was {top_reaction}, with
{top_reaction_count} reported records.

The patient age distribution indicates that the largest number of
reported cases occurred in the available age groups shown in the
evidence.

These findings are descriptive observations based only on the supplied
dataset and should not be interpreted as evidence of causality,
incidence, or a confirmed safety signal.
"""

    return narrative