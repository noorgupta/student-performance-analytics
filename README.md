# 📊 Student Performance Analytics

A full-stack student performance analytics dashboard that uses **NumPy for data analysis**, **FastAPI for the backend REST API**, and **React with Recharts for interactive data visualization**.

The application takes student performance data from a CSV dataset, performs statistical and analytical operations using NumPy, exposes the results through a FastAPI API, and presents the results through a modern React dashboard.

---

## 🚀 Live Demo

**Frontend:**  
https://student-performance-analytics-brown.vercel.app/

**Backend:**  
https://student-performance-api-qwff.onrender.com

**Live Analysis API:**  
https://student-performance-api-qwff.onrender.com/api/analysis

> **Note:** The backend is hosted on Render's free tier, so it may take a short time to wake up after a period of inactivity.

---


## 📌 Project Overview

Student Performance Analytics was created to demonstrate how Python-based data analysis can be integrated into a complete web application.

The project started as a NumPy-based data analysis program and was later extended into a full-stack application with:

- NumPy-based data processing
- FastAPI REST API
- React frontend
- Interactive charts
- Student performance tables
- Statistical analysis
- Correlation analysis
- Outlier detection
- Feature normalization

The application provides both **analytical results** and a **visual dashboard** for understanding student performance.

---

# 🎯 Objectives

The main objectives of this project are:

1. Load and process student data using NumPy.
2. Perform statistical analysis on student scores.
3. Calculate individual student performance.
4. Identify highest and lowest performers.
5. Filter students using multiple conditions.
6. Analyze relationships between study hours and performance.
7. Calculate subject-to-subject correlations.
8. Detect potential outliers.
9. Normalize numerical features.
10. Build a REST API using FastAPI.
11. Connect a React frontend to the backend.
12. Present the analysis using interactive charts and tables.

---

# ✨ Features

## 📁 Dataset Analysis

The application loads a CSV dataset containing student information.

The dataset includes:

| Column | Description |
|---|---|
| Student ID | Unique student identifier |
| Math | Mathematics score |
| Python | Python programming score |
| DSA | Data Structures and Algorithms score |
| AI/ML | Artificial Intelligence / Machine Learning score |
| Attendance | Student attendance percentage |
| Study Hours | Average study hours |

The current dataset contains:

- **10 students**
- **7 columns**
- **70 total values**
- **2 dimensions**
- **float64 data type**

---

# 📈 Statistical Analysis

The application calculates the following statistics for every subject:

- Mean
- Median
- Variance
- Standard deviation

### Example

| Subject | Mean | Median | Variance | Standard Deviation |
|---|---:|---:|---:|---:|
| Math | 72.80 | 74.00 | 245.36 | 15.66 |
| Python | 75.30 | 76.50 | 151.61 | 12.31 |
| DSA | 68.90 | 70.00 | 272.49 | 16.51 |
| AI/ML | 75.30 | 76.00 | 239.61 | 15.48 |

---

# 👨‍🎓 Student Performance Analysis

The application calculates the average score of every student using the four subject scores:

```text
Math + Python + DSA + AI/ML
--------------------------------
              4
```

Each student's average is then used to determine their overall performance.

### Performance Categories

| Average Score | Performance |
|---:|---|
| 90 and above | Excellent |
| 80–89.99 | Good |
| 60–79.99 | Average |
| Below 60 | Needs Improvement |

---

# 🏆 Highest and Lowest Performers

The application automatically identifies:

### Highest Performer

**Student 107**

Average score:

```text
93.00
```

### Lowest Performer

**Student 110**

Average score:

```text
46.25
```

---

# 🐍 Python Performance Analysis

The application uses NumPy boolean indexing to perform conditional filtering.

## Python Score > 80

Students:

```text
101, 103, 107, 109
```

Total:

```text
4 students
```

---

## Python > 80 AND Attendance > 90

Students satisfying both conditions:

```text
101, 103, 107, 109
```

The condition is implemented using NumPy's element-wise AND operator:

```python
(python_scores > 80) & (attendance > 90)
```

---

## Python > 90 OR Attendance > 95

Students satisfying at least one condition:

```text
103, 107
```

The condition is implemented using NumPy's element-wise OR operator:

```python
(python_scores > 90) | (attendance > 95)
```

---

# 🔗 Correlation Analysis

The application analyzes the relationship between:

- Study hours
- Average student score

The calculated correlation is approximately:

```text
0.9858
```

The direction is:

```text
Positive
```

This indicates a **strong positive linear relationship in the current dataset**: students who study more hours tend to have higher average scores.

Correlation is calculated using:

```python
np.corrcoef()
```

---

# 📚 Subject Correlation

The application also calculates the correlation between all subjects.

The resulting correlation matrix is:

```text
[[1.0000  0.9709  0.9973  0.9987]
 [0.9709  1.0000  0.9630  0.9723]
 [0.9973  0.9630  1.0000  0.9973]
 [0.9987  0.9723  0.9973  1.0000]]
```

The subjects are ordered as:

```text
Math
Python
DSA
AI/ML
```

This shows that the subjects have strong positive correlations within this dataset.

---

# 🚨 Outlier Detection

Potential outliers are detected using the statistical rule:

```text
Lower Bound = Mean - 2 × Standard Deviation

Upper Bound = Mean + 2 × Standard Deviation
```

A value is considered a potential outlier when:

```text
value < lower bound
```

or:

```text
value > upper bound
```

For the current dataset:

```text
Potential Outliers: 0
```

---

# ⚖️ Feature Normalization

The application uses **Min-Max normalization** to scale numerical features between 0 and 1.

The formula is:

```text
normalized value =
(value - minimum) / (maximum - minimum)
```

This is implemented using NumPy:

```python
(feature - feature_min) / (feature_max - feature_min)
```

Normalization is useful when features have different numerical ranges and need to be placed on a common scale.

---

# 🖥️ Dashboard

The React frontend converts the analysis results into an interactive dashboard.

The dashboard contains:

### Summary Cards

- Total Students
- Highest Average
- Lowest Average
- Students with Python > 80

### Performance Overview

Interactive visualization of average score by subject.

### Student Performance

Interactive chart showing the average score of every student.

### Study Hours vs Performance

Scatter plot showing the relationship between:

```text
Study Hours
      ↓
Average Score
```

The correlation coefficient is displayed alongside the chart.

### Python Performance Analysis

Displays results for:

- Python > 80
- Python > 80 AND Attendance > 90
- Python > 90 OR Attendance > 95

### Student Details

A table displaying:

- Student ID
- Average Score
- Performance level

### Highest Performer

Highlights the student with the highest average.

### Lowest Performer

Highlights the student with the lowest average.

### Outlier Analysis

Displays the number of potential outliers detected.

---

# 📊 Visualizations

The frontend uses **Recharts** to create interactive charts.

The dashboard includes:

1. Subject Performance Bar Chart
2. Student Performance Bar Chart
3. Study Hours vs Average Score Scatter Plot
4. Subject Performance Progress Indicators
5. Student Performance Table

---

# 🏗️ Application Architecture

```text
                    ┌──────────────────────┐
                    │  student_performance │
                    │       .csv            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │        NumPy         │
                    │                      │
                    │ Data Processing      │
                    │ Statistics           │
                    │ Filtering            │
                    │ Correlation          │
                    │ Outlier Detection    │
                    │ Normalization        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │                      │
                    │    REST API          │
                    │   /api/analysis      │
                    └──────────┬───────────┘
                               │
                               │ JSON
                               ▼
                    ┌──────────────────────┐
                    │        React         │
                    │                      │
                    │ Dashboard            │
                    │ Charts               │
                    │ Tables               │
                    │ Statistics           │
                    └──────────────────────┘
```

---

# 🧰 Technology Stack

## Backend

- **Python**
- **NumPy**
- **FastAPI**
- **Uvicorn**

## Frontend

- **React**
- **Vite**
- **JavaScript**
- **Recharts**
- **CSS**

## Data

- CSV

## Development Tools

- Git
- GitHub
- npm
- Python Virtual Environment

---

# 📂 Project Structure

```text
student-performance-analytics/
│
├── backend/
│   ├── analysis.py
│   └── main.py
│
├── data/
│   └── student_performance.csv
│
├── frontend/
│   ├── public/
│   │   ├── favicon.svg
│   │   └── icons.svg
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   ├── hero.png
│   │   │   ├── react.svg
│   │   │   └── vite.svg
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── outputs/
│   ├── student_performance.png
│   ├── study_hours_vs_average.png
│   └── subject_performance.png
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🔄 Backend and Frontend Flow

When the application is opened:

```text
React Frontend
      │
      │ HTTP GET
      ▼
GET /api/analysis
      │
      ▼
FastAPI
      │
      ▼
run_analysis()
      │
      ▼
load_data()
      │
      ▼
CSV Dataset
      │
      ▼
NumPy Analysis
      │
      ▼
JSON Response
      │
      ▼
React Dashboard
      │
      ▼
Charts + Tables + Statistics
```

---

# 🔌 API

The backend provides an analysis endpoint:

```text
GET /api/analysis
```

When running locally:

```text
http://127.0.0.1:8000/api/analysis
```

The API returns JSON containing:

```text
dataset
subject_statistics
student_performance
highest_performer
lowest_performer
python_analysis
correlation
outliers
normalized_features
study_hours_performance
```

---

# 📦 Example API Response

A simplified response looks like:

```json
{
  "dataset": {
    "rows": 10,
    "columns": 7,
    "dimensions": 2,
    "size": 70,
    "data_type": "float64"
  },
  "highest_performer": {
    "student_id": 107,
    "average": 93.0
  },
  "lowest_performer": {
    "student_id": 110,
    "average": 46.25
  },
  "python_analysis": {
    "count_above_80": 4
  },
  "correlation": {
    "study_hours_vs_average": 0.9858,
    "direction": "Positive"
  },
  "outliers": {
    "total": 0
  }
}
```

---

# 📖 NumPy Concepts Demonstrated

This project demonstrates practical use of the following NumPy concepts.

## Loading Data

```python
np.loadtxt()
```

Used to load the CSV dataset.

---

## Array Slicing

```python
data[:, 1:5]
```

Used to select subject scores.

---

## Mean

```python
np.mean()
```

Used to calculate average scores.

---

## Median

```python
np.median()
```

Used to calculate median subject scores.

---

## Variance

```python
np.var()
```

Used to measure score variation.

---

## Standard Deviation

```python
np.std()
```

Used to measure score dispersion.

---

## Maximum and Minimum

```python
np.max()
np.min()
```

Used to find highest and lowest values.

---

## Argmax and Argmin

```python
np.argmax()
np.argmin()
```

Used to find the index of the highest and lowest-performing students.

---

## Boolean Indexing

```python
python_scores > 80
```

Used to filter students.

---

## Multiple Conditions

AND:

```python
(condition1) & (condition2)
```

OR:

```python
(condition1) | (condition2)
```

---

## Correlation

```python
np.corrcoef()
```

Used to calculate relationships between variables.

---

## Min-Max Normalization

```python
(data - minimum) / (maximum - minimum)
```

Used to scale numerical values between 0 and 1.

---

# 🧪 Running the Project Locally

## Prerequisites

Make sure you have installed:

- Python 3
- Node.js
- npm
- Git

---

# 🐍 Backend Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Move into the project:

```bash
cd student-performance-analytics
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Start the Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

# 📚 FastAPI Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to test:

```text
GET /api/analysis
```

---

# ⚛️ Frontend Installation

Open another terminal.

Move into the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

---

# ▶️ Start the Frontend

Run:

```bash
npm run dev
```

Vite will provide a local development URL, normally:

```text
http://localhost:5173
```

Open that address in your browser.

---

# ⚙️ Running Both Servers

You need two terminals.

### Terminal 1 — Backend

From the project root:

```bash
source .venv/bin/activate
uvicorn backend.main:app --reload
```

### Terminal 2 — Frontend

From the frontend directory:

```bash
npm run dev
```

Then open the frontend URL provided by Vite.

---

# 📋 Requirements

Python dependencies are stored in:

```text
requirements.txt
```

Example:

```text
numpy==2.5.2
fastapi
uvicorn
```

Frontend dependencies are managed using:

```text
frontend/package.json
```

and:

```text
frontend/package-lock.json
```

---

# 🖼️ Generated Analysis Outputs

The original NumPy analysis also generates static visualizations.

They are stored inside:

```text
outputs/
```

Available outputs:

```text
student_performance.png
study_hours_vs_average.png
subject_performance.png
```

These files represent the analysis performed before integrating the React dashboard.

---

# 🛡️ Git and Project Hygiene

The following files and directories are excluded from version control:

```text
.venv/
__pycache__/
*.pyc
frontend/node_modules/
frontend/dist/
.env
```

This prevents unnecessary generated files and local environment files from being uploaded to GitHub.

---

# 🐛 Troubleshooting

## FastAPI Installation Error

If you see:

```text
error: externally-managed-environment
```

activate the project's virtual environment first:

```bash
source .venv/bin/activate
```

Then run:

```bash
pip install -r requirements.txt
```

---

## Frontend `vite: not found`

Move into the frontend directory:

```bash
cd frontend
```

Run:

```bash
npm install
```

Then:

```bash
npm run dev
```

---

## Frontend Cannot Connect to Backend

Make sure the FastAPI backend is running:

```bash
uvicorn backend.main:app --reload
```

Then test:

```text
http://127.0.0.1:8000/api/analysis
```

If the endpoint returns JSON, the backend is working.

---

## CORS Error

The FastAPI backend must allow requests from the React development server.

For local development, the frontend normally runs on:

```text
http://localhost:5173
```

The backend CORS configuration should therefore include the frontend development origin.

---

# 🔐 Security Considerations

This project currently uses a local CSV dataset and does not contain authentication.

For a production application, additional security could include:

- Authentication
- Authorization
- Input validation
- Secure environment variables
- HTTPS
- Rate limiting
- Database access controls
- API security
- Proper error handling

---

# 🚀 Future Improvements

The project can be extended with:

### Dataset Upload

Allow users to upload their own CSV files.

### Dynamic Analysis

Automatically analyze uploaded datasets instead of using a fixed dataset.

### Student Search

Add search functionality for individual students.

### Subject Filtering

Allow users to analyze individual subjects.

### Advanced Analytics

Add:

- Percentiles
- Quartiles
- Ranking
- Distribution analysis
- Regression analysis

### Database Integration

Replace the CSV dataset with a database such as:

- PostgreSQL
- MySQL

### Authentication

Add:

- Login
- Registration
- User accounts
- Role-based access

### Dashboard Improvements

Add:

- Date filters
- Subject filters
- Student filters
- Interactive tooltips
- More charts
- Export functionality

### Deployment

Deploy the application using cloud services.

---

# 💡 What I Learned

Through this project, I practiced:

- Python programming
- NumPy
- Numerical data analysis
- Statistical calculations
- Array manipulation
- Boolean indexing
- Data filtering
- Correlation analysis
- Outlier detection
- Feature normalization
- REST API development
- FastAPI
- React
- Recharts
- Frontend-backend integration
- JSON data handling
- Git and GitHub
- Project organization

---

# 🎓 Academic Relevance

This project demonstrates how concepts from **data analytics, Python programming, and web development** can be combined into a practical application.

It can be used as an academic project to demonstrate:

- NumPy programming
- Statistical analysis
- Data visualization
- API development
- Frontend development
- Full-stack integration

---

# 📌 Current Dataset Results

For the included dataset:

| Metric | Result |
|---|---:|
| Total Students | 10 |
| Highest Average | 93.00 |
| Lowest Average | 46.25 |
| Python > 80 | 4 |
| Study Hours Correlation | 0.9858 |
| Correlation Direction | Positive |
| Potential Outliers | 0 |

### Highest Performer

```text
Student 107
Average: 93.00
```

### Lowest Performer

```text
Student 110
Average: 46.25
```

---

# 🌟 Project Highlights

The main strength of this project is the integration of multiple technologies:

```text
NumPy
  ↓
Data Analysis
  ↓
FastAPI
  ↓
REST API
  ↓
React
  ↓
Recharts
  ↓
Interactive Dashboard
```

Instead of keeping the NumPy analysis as a terminal-only program, the project turns the analysis into a complete web-based analytics application.

---

# 👨‍💻 Author

**Noor Gupta**

Student Performance Analytics

Built using:

```text
Python • NumPy • FastAPI • React • Recharts
```

---

# 📄 License

This project is intended for educational and portfolio purposes.

You may modify and extend the project for learning and development.