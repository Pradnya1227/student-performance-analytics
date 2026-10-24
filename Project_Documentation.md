# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project title:** Student Performance Analytics System  
**Student name:** Pradnya Wakode  
**Course:** Python with AI  
**Student ID / batch:** Add your details if required by the trainer.

## 2. Objective
The objective is to analyse student marks and attendance using Python. The system automates common calculations and displays understandable results, helping identify high-performing students, subject trends, and students who need support.

## 3. Technologies Used
- **Python:** program flow, conditions, loops and reusable functions.
- **Pandas:** reading CSV data, working with DataFrames, grouping and exporting results.
- **NumPy:** numerical calculations such as mean, maximum, minimum and pass/fail selection.
- **CSV:** simple format for storing the student dataset.

## 4. Dataset Description
The project contains 20 sample student records. Each row includes a student ID, name, department, marks in Python, Mathematics, Database and AI, and attendance percentage. The dataset is fictional demonstration data and should not be presented as actual institutional records.

## 5. Implementation
1. `main.py` reads `students.csv` into a Pandas DataFrame.
2. `validate_dataset()` checks required columns, empty data and valid ranges for marks and attendance.
3. `process_students()` calculates total marks and average marks for each student.
4. `assign_grade()` applies the defined grade thresholds.
5. A student passes only when each subject mark is at least 40 and attendance is at least 75%.
6. `get_subject_summary()` uses a loop and NumPy to calculate each subject's average, highest mark and lowest mark.
7. `get_class_summary()` calculates the number of students, overall class average, highest and lowest student averages, pass/fail counts and top performers.
8. Pandas `groupby()` calculates average performance by department.
9. The final analysis is printed to the terminal, and detailed student results and subject summaries are saved as CSV files in `output/`.

## 6. Key Features
- Dataset loading and validation.
- Total and average mark calculation.
- Grade assignment.
- Pass/fail analysis.
- Class-level and subject-level statistics.
- Department-wise average analysis.
- Top performer identification.
- Export of analysis results to CSV.

## 7. Output / Screenshots
After running `python main.py`, capture a screenshot of the terminal showing the student results, class summary and subject-wise summary. Also capture the generated `output` files in the project folder if requested by the trainer. Add your genuine screenshots here before final submission.

## 8. Final Outcome
The program processes the included student dataset and produces student-level results, class statistics, subject comparisons and department averages. It demonstrates the use of Python fundamentals, NumPy and Pandas for a practical data-analysis task.

## 9. Challenges and Learning
- Organising records consistently in a CSV file.
- Checking data values before performing calculations.
- Separating calculations into reusable functions.
- Using Pandas for tabular data and NumPy for numerical operations.
- Defining explicit and consistent grading and pass/fail rules.
- Exporting results so they can be reviewed without reading the source code.

Edit this section to describe any actual challenges you personally encountered while building and testing the project.

## 10. GitHub Repository
**Repository URL:** Add the URL after creating and pushing the repository.

## Submission note
The assignment PDF requests the working project, GitHub repository, documentation and submission through the Google Form provided by EWB Courses. Upload the final repository link to that official form and verify that the submission is confirmed. The form link is not included in the assignment PDF, so obtain it from the trainer/course portal.
