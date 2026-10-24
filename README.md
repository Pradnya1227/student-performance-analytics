# Student Performance Analytics System

A beginner-friendly Python data-analysis project built with **Python, NumPy and Pandas**. It reads student marks from a CSV file, calculates totals and averages, assigns grades, checks pass/fail status, and reports class and subject performance.

## Features
- Reads 20 student records from `students.csv` using Pandas.
- Validates required columns and checks that marks/attendance are between 0 and 100.
- Calculates total and average marks for four subjects.
- Assigns grades using a clear grading scale.
- Determines pass/fail using the rule below.
- Reports class statistics, subject-wise highest/lowest/average marks, department averages and top performers.
- Exports detailed results to CSV files in `output/`.

## Technologies
- Python 3
- Pandas
- NumPy

## Grading and result rules
**Grade based on average marks:** A: 85–100, B: 70–84.99, C: 55–69.99, D: 40–54.99, F: below 40.

**Pass rule:** a student must score at least 40 in every subject and have attendance of at least 75%. Otherwise, the result is Fail. This is the project's stated rule and can be changed if the trainer specifies another rule.

## Project files
```text
student-performance-analytics/
├── main.py
├── functions.py
├── students.csv
├── requirements.txt
├── Project_Documentation.md
├── README.md
└── output/                  # generated when the program runs
```

## Setup and run
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```
5. Check the generated `output/student_results.csv` and `output/subject_summary.csv`.

On Windows, `py main.py` can be used if `python` is not recognized.

## Dataset
The included 20-row dataset is **sample/demo data**, not real student records. Columns: Student_ID, Name, Department, Python, Mathematics, Database, AI, Attendance_Percent.

## GitHub
Create a public repository named `student-performance-analytics`, then push these project files. Replace any placeholder student details in the documentation before final submission. Submit the repository URL using the official EWB Courses Google Form supplied by your trainer.
