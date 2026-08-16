import json
import os


def test_analysis_results():
    print("\n==============================")
    print("RUNNING SYSTEM TESTS")
    print("==============================")

    # Check analysis file
    assert os.path.exists(
        "output/analysis_results.json"
    ), "analysis_results.json not found"

    with open(
        "output/analysis_results.json",
        "r",
        encoding="utf-8"
    ) as file:
        analysis = json.load(file)

    # Check evidence file
    assert os.path.exists(
        "output/evidence.json"
    ), "evidence.json not found"

    with open(
        "output/evidence.json",
        "r",
        encoding="utf-8"
    ) as file:
        evidence = json.load(file)

    # Basic validation
    dataset = evidence["dataset_evidence"]
    case_data = evidence["case_evidence"]

    total_cases = dataset["total_unique_cases"]
    serious_cases = case_data["serious_cases"]
    non_serious_cases = case_data["non_serious_cases"]

    assert total_cases > 0, "Total cases should be greater than 0"

    assert (
        serious_cases + non_serious_cases == total_cases
    ), "Case counts do not match total cases"

    assert os.path.exists(
        "output/generated_report.md"
    ), "Generated report not found"

    print("✓ Analysis results file exists")
    print("✓ Evidence file exists")
    print("✓ Generated report exists")
    print(f"✓ Total cases validated: {total_cases}")
    print(f"✓ Serious cases validated: {serious_cases}")
    print(f"✓ Non-serious cases validated: {non_serious_cases}")

    print("\n==============================")
    print("ALL TESTS PASSED SUCCESSFULLY")
    print("==============================")


if __name__ == "__main__":
    test_analysis_results()