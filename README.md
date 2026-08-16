# GenAR AI Engineering Challenge

## Pharmacovigilance Safety Intelligence Platform

This project analyzes Individual Case Safety Reports (ICSRs) for Bisoprolol and generates a structured safety report using deterministic Python and Pandas analysis.

## Features

- Data validation
- Missing value analysis
- Duplicate detection
- Date validation
- Safety case analysis
- Serious and non-serious case analysis
- Patient demographic analysis
- Age group analysis
- Geographic distribution analysis
- Adverse reaction analysis
- Reaction outcome analysis
- Monthly case trend analysis
- Evidence generation
- Automated safety report generation

## Dataset

The project uses an ICSR safety dataset containing:

- Total Records: 1068
- Unique Safety Cases: 1024
- Drug: Bisoprolol
- Reporting Period: 2024-12-27 to 2025-12-26

## Project Structure

```text
GenAR-AI-Challenge/
│
├── data/
│   └── Bisoprolol_icsr_sample_1068rows (1).xlsx
│
├── src/
│   ├── validation.py
│   ├── data_loader.py
│   ├── analysis.py
│   ├── evidence_builder.py
│   └── report_generator.py
│
├── output/
│   ├── analysis_results.json
│   ├── evidence.json
│   └── generated_report.md
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Navigate to the project folder:

```bash
cd GenAR-AI-Challenge
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

Run the complete pipeline using:

```bash
python main.py
```

The pipeline performs:

1. Data Validation
2. Dataset Loading and Checking
3. Safety Analysis
4. Evidence Building
5. Safety Report Generation

## Output

After successful execution, the following files are generated:

```text
output/
├── analysis_results.json
├── evidence.json
└── generated_report.md
```

## Important Note

This project provides descriptive analysis of the supplied ICSR safety dataset.

The results should not be interpreted as incidence rates, risk estimates, or evidence of a causal relationship between Bisoprolol and reported adverse events.

Further clinical and pharmacovigilance evaluation would be required before making regulatory or causal conclusions.

## Technologies Used

- Python 3.11
- Pandas
- OpenPyXL

## Author

Sanjay Medisetti