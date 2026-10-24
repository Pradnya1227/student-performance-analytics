"""Main program for the Student Performance Analytics System."""
from pathlib import Path
import pandas as pd
from functions import (
    SUBJECTS, validate_dataset, process_students,
    get_subject_summary, get_class_summary
)

DATA_FILE = Path(__file__).with_name("students.csv")
OUTPUT_DIR = Path(__file__).with_name("output")

def main():
    try:
        students = pd.read_csv(DATA_FILE)
        students = validate_dataset(students)
    except (FileNotFoundError, pd.errors.ParserError, ValueError) as error:
        print(f"Could not load the dataset: {error}")
        return

    processed = process_students(students)
    subject_summary = get_subject_summary(students)
    class_summary = get_class_summary(processed)
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("=" * 68)
    print("           STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 68)
    print(f"\nStudents analysed: {class_summary['student_count']}")
    print("\nSTUDENT RESULTS")
    print(processed[["Student_ID", "Name", "Department", "Total_Marks",
                     "Average_Marks", "Grade", "Result"]].to_string(index=False))
    print("\nCLASS SUMMARY")
    print(f"Class average:       {class_summary['class_average']:.2f}/100")
    print(f"Highest average:     {class_summary['highest_average']:.2f}/100")
    print(f"Lowest average:      {class_summary['lowest_average']:.2f}/100")
    print(f"Students passed:     {class_summary['passed']}")
    print(f"Students failed:     {class_summary['failed']}")
    print("Top performer(s):   " + ", ".join(class_summary["top_students"]))
    print("\nSUBJECT-WISE SUMMARY")
    print(subject_summary.to_string(index=False))
    print("\nDEPARTMENT-WISE AVERAGE")
    print(processed.groupby("Department")["Average_Marks"].mean().round(2).sort_values(ascending=False).to_string())
    print("\nOUTPUT FILES")
    print(f"Detailed results: {OUTPUT_DIR / 'student_results.csv'}")
    print(f"Subject summary:  {OUTPUT_DIR / 'subject_summary.csv'}")

    processed.to_csv(OUTPUT_DIR / "student_results.csv", index=False)
    subject_summary.to_csv(OUTPUT_DIR / "subject_summary.csv", index=False)
    print("\nAnalysis completed successfully.")

if __name__ == "__main__":
    main()
