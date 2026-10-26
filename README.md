# Student Performance Analytics System

A beginner-friendly Python data-analysis project that summarizes student marks and attendance using **Python, NumPy, and Pandas**.

## Features
- Reads student records from `students.csv` with Pandas.
- Calculates each student's total and average marks.
- Assigns grades using the thresholds below.
- Identifies pass/fail students.
- Reports class averages, highest/lowest averages, and attendance.
- Calculates subject-wise averages and lists the top three students.
- Exports detailed results to `student_analysis_results.csv`.

## Grade rule
- A+: 90 and above
- A: 80–89.99
- B: 70–79.99
- C: 60–69.99
- D: 50–59.99
- E: 40–49.99
- F: below 40

A student passes only if they score at least 40 in **every subject**. These are project-defined rules and can be changed if your trainer specifies different rules.

## Requirements
- Python 3.9 or newer recommended
- pandas
- numpy

Install dependencies:
```bash
python -m pip install pandas numpy
```

## Run the project
Keep `main.py`, `functions.py`, and `students.csv` in the same folder, then run:
```bash
python main.py
```

The program displays the analysis and saves `student_analysis_results.csv` in the same folder.

## Project files
- `main.py` — main program
- `functions.py` — reusable grade, pass/fail, and display functions
- `students.csv` — sample dataset of 20 fictional student records
- `Project_Documentation.docx` — editable report
- `Project_Documentation.pdf` — report copy
- `student_analysis_results.csv` — generated when the program runs

## Dataset note
All names and records in the supplied CSV are fictional sample data for demonstration. Replace or adapt them if your instructor requires your own dataset.

## Assessment alignment
The project demonstrates variables, data types, conditions, loops/iteration, functions, NumPy numerical operations, Pandas DataFrame operations, and data analysis. No machine-learning model is required.
