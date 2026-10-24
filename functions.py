"""Reusable calculations for the Student Performance Analytics System."""
import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Database", "AI"]

def validate_dataset(df):
    """Check that required columns and valid mark/attendance ranges exist."""
    required = ["Student_ID", "Name", "Department", "Attendance_Percent"] + SUBJECTS
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))
    if df.empty:
        raise ValueError("The student dataset is empty.")
    for subject in SUBJECTS:
        df[subject] = pd.to_numeric(df[subject], errors="raise")
        if ((df[subject] < 0) | (df[subject] > 100)).any():
            raise ValueError(f"{subject} marks must be between 0 and 100.")
    df["Attendance_Percent"] = pd.to_numeric(df["Attendance_Percent"], errors="raise")
    if ((df["Attendance_Percent"] < 0) | (df["Attendance_Percent"] > 100)).any():
        raise ValueError("Attendance must be between 0 and 100.")
    return df

def assign_grade(average):
    """Grade rule: A >= 85, B >= 70, C >= 55, D >= 40, otherwise F."""
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 55:
        return "C"
    elif average >= 40:
        return "D"
    return "F"

def process_students(df):
    """Return a copy with total, average, grade, and pass/fail status."""
    result = df.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = result[SUBJECTS].mean(axis=1).round(2)
    result["Grade"] = result["Average_Marks"].apply(assign_grade)
    # Pass rule: score at least 40 in every subject and attendance at least 75%.
    passed = (result[SUBJECTS].ge(40).all(axis=1) &
              result["Attendance_Percent"].ge(75))
    result["Result"] = np.where(passed, "Pass", "Fail")
    return result

def get_subject_summary(df):
    """Summarize each subject using NumPy and Pandas."""
    rows = []
    for subject in SUBJECTS:
        marks = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(marks)), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks))
        })
    return pd.DataFrame(rows)

def get_class_summary(processed_df):
    """Calculate overall class statistics."""
    averages = processed_df["Average_Marks"].to_numpy()
    top_average = averages.max()
    top_students = processed_df.loc[processed_df["Average_Marks"] == top_average, "Name"].tolist()
    return {
        "student_count": len(processed_df),
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": round(float(np.max(averages)), 2),
        "lowest_average": round(float(np.min(averages)), 2),
        "passed": int((processed_df["Result"] == "Pass").sum()),
        "failed": int((processed_df["Result"] == "Fail").sum()),
        "top_students": top_students,
    }
