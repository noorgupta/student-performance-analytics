# Student Performance Analytics

A NumPy-based data analysis project that analyzes student academic performance using numerical computing, statistical analysis, data filtering, correlation analysis, outlier detection, normalization, and visualization.

## 📌 Project Overview

**Student Performance Analytics** is a mini data analysis project built with Python, NumPy, and Matplotlib.

The project uses a CSV dataset containing student academic and behavioral information. NumPy is used to load, process, analyze, and transform the numerical data.

The main purpose of this project is to learn and practically apply NumPy concepts by working with a real structured dataset rather than studying NumPy functions individually.

## 🎯 Project Objectives

The project aims to:

* Understand NumPy arrays and their properties
* Perform numerical calculations on structured data
* Analyze student performance
* Calculate statistical measures
* Filter students using conditions
* Analyze relationships between different features
* Detect potential outliers
* Normalize numerical features
* Visualize analysis results

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Matplotlib**
* **CSV**

## 📊 Dataset

The dataset contains information about **10 students**.

Each record contains the following fields:

| Column      | Description                                      |
| ----------- | ------------------------------------------------ |
| Student ID  | Unique identifier for each student               |
| Math        | Mathematics score                                |
| Python      | Python score                                     |
| DSA         | Data Structures & Algorithms score               |
| AI_ML       | Artificial Intelligence / Machine Learning score |
| Attendance  | Student attendance percentage                    |
| Study Hours | Student study hours                              |

The dataset contains:

* **10 students**
* **7 features/columns**
* **70 numerical values**

## 🧠 NumPy Concepts Used

This project demonstrates several important NumPy concepts.

### Array Properties

* `shape`
* `ndim`
* `size`
* `dtype`

### Indexing and Slicing

Examples include:

```python
data[:, 1:]
data[:, 1:5]
data[:, 0]
```

These operations are used to select students, subjects, and individual features from the dataset.

### Statistical Operations

The project uses:

* `np.mean()`
* `np.median()`
* `np.min()`
* `np.max()`
* `np.var()`
* `np.std()`

### Finding Maximum and Minimum

The project uses:

* `np.argmax()`
* `np.argmin()`

to identify the highest- and lowest-performing students.

### Boolean Indexing

Students are filtered using conditions such as:

```python
python_scores > 80
```

Multiple conditions are also used with:

```python
&
|
```

### Correlation Analysis

The project uses:

```python
np.corrcoef()
```

to analyze relationships between:

* Study hours and average score
* Different subject scores

### Outlier Detection

Potential outliers are identified using the rule:

```text
Mean ± 2 × Standard Deviation
```

### `np.where()`

`np.where()` is used to locate the exact rows and columns containing potential outliers.

### Broadcasting

NumPy broadcasting is used during calculations such as:

```python
means - 2 * std
```

and during feature normalization.

### Min-Max Normalization

The project normalizes numerical features using:

```text
(value - minimum) / (maximum - minimum)
```

This transforms values to a range between **0 and 1**.

## 🔍 Analysis Performed

### 1. Dataset Exploration

The program displays:

* Dataset shape
* Number of dimensions
* Total number of elements
* Data type

### 2. Subject-Wise Analysis

For each subject, the project calculates:

* Mean
* Median
* Variance
* Standard deviation

### 3. Student Average Performance

The average of the four subject scores is calculated for every student.

The project identifies:

* Highest-performing student
* Lowest-performing student

### 4. Conditional Student Filtering

The project identifies students based on conditions such as:

* Python score greater than 80
* Python score greater than 80 **AND** attendance greater than 90
* Python score greater than 90 **OR** attendance greater than 95

### 5. Correlation Analysis

The relationship between study hours and average score is calculated.

The project also generates a correlation matrix showing relationships between different subjects.

### 6. Outlier Detection

Potential subject-score outliers are detected using the mean ± 2 standard deviation method.

The project also identifies:

* Student ID
* Subject containing the potential outlier

### 7. Feature Normalization

All numerical features are normalized using Min-Max normalization.

This produces values between:

```text
0 and 1
```

## 📈 Visualizations

The project generates three visualizations.

### Average Score by Subject

A bar chart comparing the average scores of:

* Math
* Python
* DSA
* AI/ML

Saved as:

```text
outputs/subject_performance.png
```

### Study Hours vs Average Score

A scatter plot showing the relationship between study hours and overall average score.

Saved as:

```text
outputs/study_hours_vs_average.png
```

### Student Average Performance

A bar chart comparing the average score of every student.

Saved as:

```text
outputs/student_performance.png
```

## 📋 Current Results

Based on the current dataset:

| Analysis                                 | Result      |
| ---------------------------------------- | ----------- |
| Highest Performing Student               | Student 107 |
| Highest Average                          | 93.00       |
| Lowest Performing Student                | Student 110 |
| Lowest Average                           | 46.25       |
| Students with Python > 80                | 4           |
| Study Hours vs Average Score Correlation | 0.9858      |
| Potential Subject Outliers               | 0           |

The study-hours correlation of **0.9858** indicates a very strong positive linear relationship within this particular dataset.

This result should not be generalized because the dataset contains only 10 students.

## 📁 Project Structure

```text
student-performance-analytics/
│
├── data/
│   └── student_performance.csv
│
├── outputs/
│   ├── subject_performance.png
│   ├── study_hours_vs_average.png
│   └── student_performance.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd student-performance-analytics
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

On Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Install the required packages using the existing `requirements.txt`:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

Run:

```bash
python3 main.py
```

The analysis results will be displayed in the terminal.

The generated visualizations will be saved in:

```text
outputs/
```

## 📦 Dependencies

The project uses:

```text
numpy
matplotlib
```

The exact installed versions are maintained in:

```text
requirements.txt
```

## 🧪 Example Workflow

The project follows this general data-analysis workflow:

```text
CSV Dataset
     ↓
Load Data with NumPy
     ↓
Explore Array Properties
     ↓
Select Features
     ↓
Calculate Statistics
     ↓
Analyze Student Performance
     ↓
Filter Data
     ↓
Calculate Correlations
     ↓
Detect Potential Outliers
     ↓
Normalize Features
     ↓
Visualize Results
```

## 🎓 Learning Outcomes

By completing this project, I practiced using NumPy for:

* Numerical data processing
* Array manipulation
* Indexing and slicing
* Statistical calculations
* Boolean indexing
* Conditional filtering
* Correlation analysis
* Outlier detection
* Broadcasting
* Feature normalization
* Vectorized numerical operations

The project also provided practical experience in organizing Python functions and combining numerical analysis with data visualization.

## 🚀 Future Improvements

Possible future improvements include:

* Using a larger and more realistic dataset
* Adding additional statistical analysis
* Adding more visualizations
* Introducing Pandas for tabular data analysis
* Building an interactive dashboard
* Applying machine learning algorithms
* Predicting student performance
* Comparing different machine learning models

## 👨‍💻 Project Purpose

This project was created as a practical learning project to strengthen Python and NumPy fundamentals before progressing toward **Machine Learning**.

The focus is on understanding the concepts behind numerical data analysis and applying them through a complete, hands-on project.
