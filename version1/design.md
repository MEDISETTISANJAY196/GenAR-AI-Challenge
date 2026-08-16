# GenAR AI Engineering Challenge - Version 1 Design

## Project Title

GenAR Pharmacovigilance Safety Intelligence Platform

---

## 1. Problem Statement

Pharmacovigilance teams need to review large volumes of Individual Case Safety Reports (ICSRs) to understand reported adverse events, patient demographics, case seriousness, reaction outcomes, and reporting trends.

Manual review can be time-consuming and makes it difficult to quickly create a structured evidence summary.

This project provides a Python-based safety intelligence pipeline that processes a supplied ICSR dataset for Bisoprolol and generates structured evidence and a safety report for human review.

---

## 2. Proposed Solution

The system follows a deterministic data-processing pipeline:

```text
ICSR Excel Dataset
        ↓
Data Validation
        ↓
Data Loading and Cleaning
        ↓
Safety Case Analysis
        ↓
Structured Evidence Generation
        ↓
Automated Safety Report
        ↓
Streamlit Dashboard
        ↓
Human Review