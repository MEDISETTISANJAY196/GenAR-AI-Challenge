# System Architecture

## GenAR Pharmacovigilance Safety Intelligence Platform

The system follows a structured pipeline for transforming raw Individual Case Safety Reports (ICSRs) into evidence and a generated safety report.

```mermaid
flowchart TD

A[ICSR Dataset - Excel] --> B[Data Validation]

B --> C[Data Loading and Cleaning]

C --> D[Safety Analysis]

D --> E[Evidence Building]

E --> F[AI / Report Generation Layer]

F --> G[Human Review]

G --> H[Final PADER Style Safety Report]