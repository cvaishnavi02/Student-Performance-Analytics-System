import pandas as pd
import numpy as np
from functions import assign_grade, get_pass_status, print_section

DATA_FILE = "students.csv"
PASS_MARK = 40

def analyze_students(data):
    """Add total, average, grade, and pass/fail columns to the student data."""
    subject_columns = ["Python", "Mathematics", "AI", "Data Analysis"]

    data["Total"] = data[subject_columns].sum(axis=1)
    data["Average"] = data[subject_columns].mean(axis=1).round(2)
    data["Grade"] = data["Average"].apply(assign_grade)
    data["Result"] = data[subject_columns].apply(
        lambda row: get_pass_status(row, PASS_MARK), axis=1
    )
    return data

def main():
    try:
        students = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"Error: {DATA_FILE} was not found. Keep it in the same folder as main.py.")
        return

    subject_columns = ["Python", "Mathematics", "AI", "Data Analysis"]
    required_columns = ["Student ID", "Name", "Department", "Attendance"] + subject_columns
    missing = [column for column in required_columns if column not in students.columns]
    if missing:
        print("Dataset is missing these columns:", ", ".join(missing))
        return

    print_section("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print(f"Number of students: {len(students)}")
    print("\nDataset preview:")
    print(students.head().to_string(index=False))

    students = analyze_students(students)

    print_section("STUDENT-WISE RESULTS")
    print(students[["Student ID", "Name", "Total", "Average", "Grade", "Result"]].to_string(index=False))

    print_section("CLASS SUMMARY")
    print(f"Class average: {students['Average'].mean():.2f}")
    print(f"Highest student average: {students['Average'].max():.2f}")
    print(f"Lowest student average: {students['Average'].min():.2f}")
    print(f"Students passed: {(students['Result'] == 'Pass').sum()}")
    print(f"Students failed: {(students['Result'] == 'Fail').sum()}")
    print(f"Average attendance: {students['Attendance'].mean():.2f}%")

    print_section("SUBJECT-WISE AVERAGES")
    subject_averages = students[subject_columns].mean().round(2)
    for subject, average in subject_averages.items():
        print(f"{subject}: {average:.2f}")

    print_section("TOP PERFORMERS")
    top_students = students.sort_values("Average", ascending=False).head(3)
    print(top_students[["Student ID", "Name", "Average", "Grade"]].to_string(index=False))

    output_file = "student_analysis_results.csv"
    students.to_csv(output_file, index=False)
    print(f"\nDetailed results saved to {output_file}")

if __name__ == "__main__":
    main()
