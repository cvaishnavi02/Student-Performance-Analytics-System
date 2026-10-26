import numpy as np

def assign_grade(average):
    """Assign a grade using the project's stated average-mark thresholds."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    return "F"

def get_pass_status(marks, pass_mark=40):
    """A student passes only when every subject mark reaches the pass mark."""
    values = np.asarray(marks, dtype=float)
    return "Pass" if np.all(values >= pass_mark) else "Fail"

def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
