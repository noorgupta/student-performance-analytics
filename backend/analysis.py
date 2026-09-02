import numpy as np


DATA_PATH = "data/student_performance.csv"


def load_data():
    return np.loadtxt(
        DATA_PATH,
        delimiter=",",
        skiprows=1
    )


def run_analysis():
    data = load_data()

    student_ids = data[:, 0]
    subject_scores = data[:, 1:5]
    features = data[:, 1:]

    subjects = np.array([
        "Math",
        "Python",
        "DSA",
        "AI_ML"
    ])

    # Subject statistics
    subject_means = np.mean(subject_scores, axis=0)
    subject_medians = np.median(subject_scores, axis=0)
    subject_variance = np.var(subject_scores, axis=0)
    subject_std = np.std(subject_scores, axis=0)

    # Student averages
    student_averages = np.mean(
        subject_scores,
        axis=1
    )

    highest_index = np.argmax(student_averages)
    lowest_index = np.argmin(student_averages)

    highest_student = int(student_ids[highest_index])
    highest_average = float(
        student_averages[highest_index]
    )

    lowest_student = int(student_ids[lowest_index])
    lowest_average = float(
        student_averages[lowest_index]
    )

    # Python filtering
    python_scores = data[:, 2]
    attendance = data[:, 5]

    high_python_mask = python_scores > 80

    high_python_students = (
        student_ids[high_python_mask]
    )

    # AND condition
    and_mask = (
        (python_scores > 80) &
        (attendance > 90)
    )

    students_and = student_ids[and_mask]

    # OR condition
    or_mask = (
        (python_scores > 90) |
        (attendance > 95)
    )

    students_or = student_ids[or_mask]

    # Count
    count_high_python = np.sum(
        python_scores > 80
    )

    # Study hours correlation
    study_hours = data[:, 6]

    correlation_matrix = np.corrcoef(
        study_hours,
        student_averages
    )

    correlation = correlation_matrix[0, 1]

    if correlation > 0:
        direction = "Positive"
    elif correlation < 0:
        direction = "Negative"
    else:
        direction = "No linear correlation"

    # Subject correlation
    subject_correlation = np.corrcoef(
        subject_scores,
        rowvar=False
    )

    # Outlier detection
    lower_bounds = (
        subject_means - 2 * subject_std
    )

    upper_bounds = (
        subject_means + 2 * subject_std
    )

    outlier_mask = (
        (subject_scores < lower_bounds) |
        (subject_scores > upper_bounds)
    )

    total_outliers = int(
        np.sum(outlier_mask)
    )

    # Normalization
    feature_min = np.min(
        features,
        axis=0
    )

    feature_max = np.max(
        features,
        axis=0
    )

    normalized_features = (
        (features - feature_min) /
        (feature_max - feature_min)
    )

    return {
        "dataset": {
            "rows": int(data.shape[0]),
            "columns": int(data.shape[1]),
            "dimensions": int(data.ndim),
            "size": int(data.size),
            "data_type": str(data.dtype)
        },

        "subject_statistics": {
            subject: {
                "mean": float(subject_means[i]),
                "median": float(subject_medians[i]),
                "variance": float(subject_variance[i]),
                "standard_deviation": float(subject_std[i])
            }
            for i, subject in enumerate(subjects)
        },

        "student_performance": [
            {
                "student_id": int(student_ids[i]),
                "average": float(student_averages[i])
            }
            for i in range(len(student_ids))
        ],

        "highest_performer": {
            "student_id": highest_student,
            "average": highest_average
        },

        "lowest_performer": {
            "student_id": lowest_student,
            "average": lowest_average
        },

        "python_analysis": {
            "students_above_80": [
                int(student)
                for student in high_python_students
            ],
            "count_above_80": int(
                count_high_python
            ),
            "python_above_80_and_attendance_above_90": [
                int(student)
                for student in students_and
            ],
            "python_above_90_or_attendance_above_95": [
                int(student)
                for student in students_or
            ]
        },

        "correlation": {
            "study_hours_vs_average": float(
                correlation
            ),
            "direction": direction,
            "subject_correlation_matrix": (
                subject_correlation.tolist()
            )
        },

        "outliers": {
            "total": total_outliers
        },

        "normalized_features": (
            normalized_features.tolist()
        ),


        "study_hours_performance": [
        {
        "student_id": int(student_ids[i]),
        "study_hours": float(study_hours[i]),
        "average": float(student_averages[i])
        }
        for i in range(len(student_ids))
        ],
    }