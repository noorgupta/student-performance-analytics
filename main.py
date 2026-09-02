import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. Load Dataset
# ============================================================

def load_data(file_path):
    return np.loadtxt(
        file_path,
        delimiter=",",
        skiprows=1
    )


# ============================================================
# 2. Basic Dataset Information
# ============================================================

def show_dataset_info(data):
    print("\n===== Dataset Information =====")
    print("Shape:", data.shape)
    print("Dimensions:", data.ndim)
    print("Size:", data.size)
    print("Data Type:", data.dtype)


# ============================================================
# 3. Calculate Feature Means
# ============================================================

def calculate_means(data):
    return np.mean(data, axis=0)


# ============================================================
# 4. Calculate Student Averages
# ============================================================

def calculate_student_averages(data):
    return np.mean(data, axis=1)


# ============================================================
# 5. Find Highest Performing Student
# ============================================================

def find_highest_student(student_averages, student_ids):
    highest_index = np.argmax(student_averages)
    highest_average = np.max(student_averages)
    highest_student = student_ids[highest_index]

    return highest_student, highest_average


# ============================================================
# 6. Find Lowest Performing Student
# ============================================================

def find_lowest_student(student_averages, student_ids):
    lowest_index = np.argmin(student_averages)
    lowest_average = np.min(student_averages)
    lowest_student = student_ids[lowest_index]

    return lowest_student, lowest_average


# ============================================================
# 7. Calculate Median
# ============================================================

def calculate_median(data):
    return np.median(data, axis=0)


# ============================================================
# 8. Calculate Variance
# ============================================================

def calculate_variance(data):
    return np.var(data, axis=0)


# ============================================================
# 9. Calculate Standard Deviation
# ============================================================

def calculate_standard_deviation(data):
    return np.std(data, axis=0)


# ============================================================
# 10. Filter Students
# ============================================================

def filter_students(student_ids, condition):
    return student_ids[condition]


# ============================================================
# 11. Calculate Correlation
# ============================================================

def calculate_correlation(x, y):
    correlation_matrix = np.corrcoef(x, y)

    return correlation_matrix[0, 1]


# ============================================================
# 12. Detect Outliers
# ============================================================

def detect_outliers(data):
    means = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    lower_bounds = means - 2 * std
    upper_bounds = means + 2 * std

    return (
        (data < lower_bounds) |
        (data > upper_bounds)
    )


# ============================================================
# 13. Normalize Features
# ============================================================

def normalize_features(data):
    minimum = np.min(data, axis=0)
    maximum = np.max(data, axis=0)

    return (data - minimum) / (maximum - minimum)


# ============================================================
# 14. Main Analysis
# ============================================================

def main():

    # --------------------------------------------------------
    # Load data
    # --------------------------------------------------------

    data = load_data("data/student_performance.csv")

    # Separate IDs and features
    student_ids = data[:, 0]

    features = data[:, 1:]

    # First four columns after ID = subjects
    subject_scores = data[:, 1:5]

    subjects = np.array([
        "Math",
        "Python",
        "DSA",
        "AI_ML"
    ])

    # Other features
    python_scores = data[:, 2]
    attendance = data[:, 5]
    study_hours = data[:, 6]


    # --------------------------------------------------------
    # Basic Dataset Information
    # --------------------------------------------------------

    show_dataset_info(data)


    # --------------------------------------------------------
    # Subject Means
    # --------------------------------------------------------

    subject_means = calculate_means(subject_scores)

    print("\n===== Subject Means =====")

    for subject, mean in zip(subjects, subject_means):
        print(f"{subject}: {mean:.2f}")


    # --------------------------------------------------------
    # Student Averages
    # --------------------------------------------------------

    student_averages = calculate_student_averages(subject_scores)

    print("\n===== Student Averages =====")

    for student, average in zip(student_ids, student_averages):
        print(f"Student {int(student)}: {average:.2f}")


    # --------------------------------------------------------
    # Highest Performer
    # --------------------------------------------------------

    highest_student, highest_average = find_highest_student(
        student_averages,
        student_ids
    )

    print("\n===== Highest Performer =====")
    print("Student ID:", int(highest_student))
    print("Average:", round(highest_average, 2))


    # --------------------------------------------------------
    # Lowest Performer
    # --------------------------------------------------------

    lowest_student, lowest_average = find_lowest_student(
        student_averages,
        student_ids
    )

    print("\n===== Lowest Performer =====")
    print("Student ID:", int(lowest_student))
    print("Average:", round(lowest_average, 2))


    # --------------------------------------------------------
    # Median
    # --------------------------------------------------------

    median_values = calculate_median(subject_scores)

    print("\n===== Subject Median =====")

    for subject, median in zip(subjects, median_values):
        print(f"{subject}: {median:.2f}")


    # --------------------------------------------------------
    # Variance
    # --------------------------------------------------------

    subject_variance = calculate_variance(subject_scores)

    print("\n===== Subject Variance =====")

    for subject, variance in zip(subjects, subject_variance):
        print(f"{subject}: {variance:.2f}")


    # --------------------------------------------------------
    # Standard Deviation
    # --------------------------------------------------------

    subject_std = calculate_standard_deviation(subject_scores)

    print("\n===== Subject Standard Deviation =====")

    for subject, std in zip(subjects, subject_std):
        print(f"{subject}: {std:.2f}")


    # --------------------------------------------------------
    # Python Score Filtering
    # --------------------------------------------------------

    high_python_students = filter_students(
        student_ids,
        python_scores > 80
    )

    print("\n===== Python Score > 80 =====")
    print("Students:", high_python_students.astype(int))

    print(
        "Number of students:",
        len(high_python_students)
    )


    # --------------------------------------------------------
    # Multiple Conditions - AND
    # --------------------------------------------------------

    condition_and = (
        (python_scores > 80) &
        (attendance > 90)
    )

    students_and = filter_students(
        student_ids,
        condition_and
    )

    print("\n===== Python > 80 AND Attendance > 90 =====")
    print("Students:", students_and.astype(int))


    # --------------------------------------------------------
    # Multiple Conditions - OR
    # --------------------------------------------------------

    condition_or = (
        (python_scores > 90) |
        (attendance > 95)
    )

    students_or = filter_students(
        student_ids,
        condition_or
    )

    print("\n===== Python > 90 OR Attendance > 95 =====")
    print("Students:", students_or.astype(int))


    # --------------------------------------------------------
    # Study Hours vs Average Score Correlation
    # --------------------------------------------------------

    correlation = calculate_correlation(
        study_hours,
        student_averages
    )

    print("\n===== Study Hours vs Average Score =====")
    print("Correlation:", round(correlation, 4))

    if correlation > 0:
        print("Direction: Positive")
    elif correlation < 0:
        print("Direction: Negative")
    else:
        print("Direction: No linear correlation")


    # --------------------------------------------------------
    # Subject Correlation
    # --------------------------------------------------------

    subject_correlation = np.corrcoef(
        subject_scores,
        rowvar=False
    )

    print("\n===== Subject Correlation Matrix =====")
    print(subject_correlation)


    # --------------------------------------------------------
    # Outlier Detection
    # --------------------------------------------------------

    outlier_mask = detect_outliers(subject_scores)

    total_outliers = np.sum(outlier_mask)

    print("\n===== Outlier Analysis =====")
    print("Total Potential Outliers:", total_outliers)


    # Find exact outlier positions
    outlier_rows, outlier_columns = np.where(
        outlier_mask
    )

    outlier_students = student_ids[outlier_rows]
    outlier_subjects = subjects[outlier_columns]

    if total_outliers > 0:
        print("\nPotential Outliers:")

        for student, subject in zip(
            outlier_students,
            outlier_subjects
        ):
            print(
                f"Student {int(student)} - {subject}"
            )
    else:
        print("No potential outliers detected.")


    # --------------------------------------------------------
    # Feature Normalization
    # --------------------------------------------------------

    normalized_features = normalize_features(features)

    print("\n===== Normalized Features =====")
    print(normalized_features)




    # --------------------------------------------------------
    # Subject Performance Visualization
    # --------------------------------------------------------

    plt.bar(subjects, subject_means)

    plt.title("Average Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")

    plt.ylim(0, 100)

    plt.savefig("outputs/subject_performance.png")    
    plt.close()


    # --------------------------------------------------------
    # Study Hours vs Average Score Visualization
    # --------------------------------------------------------

    plt.scatter(study_hours, student_averages)

    plt.title("Study Hours vs Average Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Average Score")

    plt.savefig("outputs/study_hours_vs_average.png")
    plt.close()

    print(
        "Study hours vs average score chart "
       
        "saved as study_hours_vs_average.png"
    )

    # --------------------------------------------------------
    # Student Performance Visualization
    # --------------------------------------------------------

    plt.bar(
        student_ids.astype(int).astype(str),
        student_averages
    )

    plt.title("Student Average Performance")
    plt.xlabel("Student ID")
    plt.ylabel("Average Score")

    plt.ylim(0, 100)

    plt.savefig("outputs/student_performance.png")
    plt.close()

    print(
        "Student performance chart "
        "saved as student_performance.png"
    )


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()