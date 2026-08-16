# GenAR AI Engineering Challenge

## Pharmacovigilance Safety Intelligence System

An AI-assisted pharmacovigilance safety analysis system designed to process Individual Case Safety Report (ICSR) data and generate a structured Periodic Adverse Drug Experience Report.

The system follows an evidence-first architecture where dataset validation and deterministic analysis are completed before controlled narrative generation and report creation.

---

## Problem Statement

Pharmacovigilance teams must analyze large volumes of Individual Case Safety Reports (ICSRs) to identify adverse drug reactions, case seriousness, demographic patterns, geographic distribution, and reporting trends.

Manual analysis can be time-consuming and may create inconsistencies in reporting.

This project provides a structured pipeline that:

- Validates the supplied safety dataset
- Analyzes adverse event data
- Calculates safety metrics deterministically
- Builds a structured evidence layer
- Generates a controlled safety narrative
- Produces a Periodic Adverse Drug Experience Report
- Includes automated system validation tests

---

## System Architecture

```text
ICSR Dataset
     │
     ▼
Data Validation
     │
     ▼
Data Loading
     │
     ▼
Deterministic Safety Analysis
     │
     ▼
Structured Evidence Builder
     │
     ├───────────────┐
     ▼               │
Controlled Narrative │
Generation Layer     │
     │               │
     └───────┬───────┘
             ▼
     Report Generation
             │
             ▼
      Generated Outputs

---

---

## Project Structure

```text
GenAR-AI-Challenge/
│
├── src/
│   ├── validation.py
│   ├── data_loader.py
│   ├── analysis.py
│   ├── evidence_builder.py
│   ├── llm.py
│   ├── report_generator.py
│   └── test.py
│
├── output/
│   ├── analysis_results.json
│   ├── evidence.json
│   └── generated_report.md
│
├── prompts/
├── version1/
├── main.py
├── app.py
├── requirements.txt
├── architecture.md
└── README.md
```

---

## Key Features

### Data Validation

The system validates:

- Required columns
- Missing values
- Duplicate records
- Repeated safety report IDs
- Date validity
- Reporting period

### Deterministic Safety Analysis

The analysis calculates:

- Total dataset records
- Unique safety cases
- Serious and non-serious cases
- Patient sex distribution
- Patient age distribution
- Geographic distribution
- Most frequently reported reactions
- Reactions in serious cases
- Reaction outcomes
- Monthly case trends

### Evidence-First Architecture

```text
Analysis
   ↓
Evidence JSON
   ↓
Narrative Generation
   ↓
Final Report
```

All numerical analysis is completed before narrative generation.

### Controlled Narrative Generation

The project includes:

```text
src/llm.py
```

This module generates descriptive safety text using structured evidence produced by the deterministic analysis pipeline.

No external API key is required.

### Human Review and Approval

The application includes a human review stage before final report approval.

The reviewer remains responsible for evaluating the generated findings and making any final clinical, medical, or regulatory decisions.

---

## Automated Testing

System validation is available through:

```text
src/test.py
```

The tests verify:

- Analysis results file availability
- Evidence file availability
- Generated report availability
- Total case count
- Serious case count
- Non-serious case count

Run the tests:

```bash
python src/test.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MEDISETTISANJAY196/GenAR-AI-Challenge.git
```

Navigate to the project:

```bash
cd GenAR-AI-Challenge
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Dataset Setup

Place the supplied ICSR dataset inside:

```text
data/
```

Expected file:

```text
data/Bisoprolol_icsr_sample_1068rows (1).xlsx
```

The dataset is excluded from the GitHub repository using `.gitignore`.

---

## Running the Project

Run the complete pipeline:

```bash
python main.py
```

The pipeline performs:

```text
STEP 1 → Data Validation
STEP 2 → Dataset Loading
STEP 3 → Safety Analysis
STEP 4 → Evidence Building
STEP 5 → Report Generation
```

Run system tests:

```bash
python src/test.py
```

---

## Example Results

For the supplied dataset:

- Total Records: 1068
- Unique Safety Cases: 1024
- Serious Cases: 1023
- Non-Serious Cases: 1
- Reporting Period: 2024-12-27 to 2025-12-26
- Most Frequently Reported Reaction: Acute kidney injury

These results are descriptive outputs generated from the supplied dataset.

---

## Important Limitations

- The system performs descriptive analysis of the supplied dataset.
- Reported adverse events do not establish causality.
- Counts should not be interpreted as incidence rates or estimates of risk.
- Generated findings require appropriate medical, clinical, pharmacovigilance, or regulatory review.
- The current narrative generation layer does not use an external LLM API.

---

## Technology Stack

- Python
- Pandas
- OpenPyXL
- JSON
- Streamlit
- Deterministic Data Analysis
- Evidence-Based Narrative Generation
- Markdown Report Generation

---

## Author

**Sanjay Medisetti**

AI / Machine Learning Engineering

GitHub: https://github.com/MEDISETTISANJAY196

---

## Disclaimer

This project was developed for the GenAR AI Engineering Challenge.

It is intended for educational and technical demonstration purposes and should not be used as a substitute for professional pharmacovigilance, medical, clinical, or regulatory assessment.