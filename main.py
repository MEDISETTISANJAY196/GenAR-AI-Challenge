import subprocess
import sys

print("\n" + "=" * 50)
print("GenAR AI ENGINEERING CHALLENGE")
print("Pharmacovigilance Safety Intelligence")
print("=" * 50)

scripts = [
    ("STEP 1: Data Validation", "src/validation.py"),
    ("STEP 2: Loading and Checking Dataset", "src/data_loader.py"),
    ("STEP 3: Running Safety Analysis", "src/analysis.py"),
    ("STEP 4: Building Evidence", "src/evidence_builder.py"),
    ("STEP 5: Generating Safety Report", "src/report_generator.py"),
]

for title, script in scripts:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    result = subprocess.run(
        [sys.executable, script]
    )

    if result.returncode != 0:
        print(f"\nERROR: {script} run avvaledhu.")
        print("Project stopped.")
        sys.exit(1)

print("\n" + "=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 50)

print("\nGenerated Output Files:")
print("1. output/analysis_results.json")
print("2. output/evidence.json")
print("3. output/generated_report.md")

print("\nThank you!")