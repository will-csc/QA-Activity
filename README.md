# QA Activity: Stark Bank

> **Note to Rodrigo:** I chose to write this documentation in English to practice the language in a technical context.

This repository contains the artifacts from the Manual QA practical activity performed on the "Stark Bank" system.

## Project Files

- **`banco_stark.py`**: Python script that simulates the banking system and executes the test scenarios (SUT - System Under Test).
- **`Relatorio_QA_BancoStark.txt`**: Final report containing:
  - 3 Test Cases (Business rule validation).
  - 3 Bug Reports (Documentation of found failures).

## Objective

The goal of the activity was to transform the practical execution into formal Test Cases and register professional Bug Reports for the failures found in the simplified banking system.

## Summary of Bugs Found

During the execution of exploratory and negative tests, serious input validation failures were identified:

1.  **Transfer with negative value (Critical)**: The system allows transferring negative values, which reverses the operation logic (origin receives and destination loses), enabling fraud.
2.  **Deposit with negative value (High)**: The system accepts negative deposits, reducing the client's balance without withdrawal authorization.
3.  **Deposit with zero value (Low)**: The system allows 0 value transactions, generating unnecessary records in the statement.

## How to Run

To reproduce the tests and verify the evidences in the terminal:

```bash
python banco_stark.py
```

This will execute the "Happy Path" scenario, the expected "Negative Tests", and the "Additional Tests" created to expose critical failures.
