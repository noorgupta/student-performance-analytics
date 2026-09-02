import { useEffect, useState } from 'react'

import {
  BarChart,
  Bar,
  ScatterChart,
  Scatter,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from 'recharts'

import './App.css'


function App() {

  const [analysis, setAnalysis] = useState(null)
  const [error, setError] = useState(null)


  // Fetch data from FastAPI
  useEffect(() => {

    fetch('http://127.0.0.1:8000/api/analysis')

      .then((response) => {

        if (!response.ok) {
          throw new Error('Failed to fetch analysis')
        }

        return response.json()

      })

      .then((data) => {
        setAnalysis(data)
      })

      .catch((error) => {
        setError(error.message)
      })

  }, [])


  // Error state
  if (error) {

    return (
      <div className="app">
        <h2>Error: {error}</h2>
      </div>
    )

  }


  // Loading state
  if (!analysis) {

    return (
      <div className="app">
        <h2>Loading...</h2>
      </div>
    )

  }


  const subjects = analysis.subject_statistics


  // Subject chart data
  const subjectChartData = Object.entries(subjects).map(
    ([subject, values]) => ({
      subject,
      average: values.mean
    })
  )


  // Student chart data
  const studentChartData = analysis.student_performance.map(
    (student) => ({
      student: `Student ${student.student_id}`,
      average: student.average
    })
  )


  // Study hours chart data
  const studyHoursChartData =
    analysis.study_hours_performance.map(
      (student) => ({
        student: student.student_id,
        studyHours: student.study_hours,
        average: student.average
      })
    )


  // Performance classification
  const getPerformanceLevel = (average) => {

    if (average >= 85) {
      return 'Excellent'
    }

    if (average >= 70) {
      return 'Good'
    }

    if (average >= 50) {
      return 'Average'
    }

    return 'Needs Improvement'

  }


  return (

    <div className="app">


      {/* ================= HEADER ================= */}

      <header className="header">

        <div>

          <h1>
            Student Performance Analytics
          </h1>

          <p>
            NumPy-powered student performance dashboard
          </p>

        </div>


        <div className="badge">
          NumPy Analysis
        </div>

      </header>



      <main>


        {/* ================= SUMMARY ================= */}

        <section className="summary-grid">


          <div className="card">

            <p>Total Students</p>

            <h2>
              {analysis.dataset.rows}
            </h2>

          </div>


          <div className="card">

            <p>Highest Average</p>

            <h2>
              {analysis.highest_performer.average.toFixed(2)}
            </h2>

          </div>


          <div className="card">

            <p>Lowest Average</p>

            <h2>
              {analysis.lowest_performer.average.toFixed(2)}
            </h2>

          </div>


          <div className="card">

            <p>Python &gt; 80</p>

            <h2>
              {analysis.python_analysis.count_above_80}
            </h2>

          </div>


        </section>



        {/* ================= SUBJECT PERFORMANCE ================= */}

        <section className="section">

          <div className="section-header">

            <h2>
              Performance Overview
            </h2>

            <p>
              Average score by subject
            </p>

          </div>


          <div className="chart-container">

            <ResponsiveContainer
              width="100%"
              height={300}
            >

              <BarChart
                data={subjectChartData}
              >

                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  dataKey="subject"
                />

                <YAxis
                  domain={[0, 100]}
                />

                <Tooltip />

                <Bar
                  dataKey="average"
                  name="Average Score"
                />

              </BarChart>

            </ResponsiveContainer>

          </div>


          {/* Subject progress bars */}

          <div className="subjects">

            {Object.entries(subjects).map(
              ([subject, values]) => (

                <div
                  className="subject"
                  key={subject}
                >

                  <div className="subject-info">

                    <span>
                      {subject}
                    </span>

                    <strong>
                      {values.mean.toFixed(2)}
                    </strong>

                  </div>


                  <div className="progress">

                    <div
                      className="progress-fill"
                      style={{
                        width: `${values.mean}%`
                      }}
                    ></div>

                  </div>

                </div>

              )
            )}

          </div>

        </section>



        {/* ================= STUDENT PERFORMANCE ================= */}

        <section className="section">

          <div className="section-header">

            <h2>
              Student Performance
            </h2>

            <p>
              Average score of each student
            </p>

          </div>


          <div className="chart-container student-chart">

            <ResponsiveContainer
              width="100%"
              height={350}
            >

              <BarChart
                data={studentChartData}
                margin={{
                  top: 10,
                  right: 20,
                  left: 10,
                  bottom: 50
                }}
              >

                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  dataKey="student"
                  angle={-45}
                  textAnchor="end"
                  interval={0}
                />

                <YAxis
                  domain={[0, 100]}
                />

                <Tooltip />

                <Bar
                  dataKey="average"
                  name="Average Score"
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </section>



        {/* ================= STUDY HOURS ================= */}

        <section className="section">

          <div className="section-header">

            <h2>
              Study Hours vs Performance
            </h2>

            <p>
              Relationship between study hours
              and average score
            </p>

          </div>


          <div className="chart-container">

            <ResponsiveContainer
              width="100%"
              height={350}
            >

              <ScatterChart
                margin={{
                  top: 20,
                  right: 20,
                  bottom: 20,
                  left: 10
                }}
              >

                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  type="number"
                  dataKey="studyHours"
                  name="Study Hours"
                />

                <YAxis
                  type="number"
                  dataKey="average"
                  name="Average Score"
                  domain={[0, 100]}
                />

                <Tooltip />

                <Scatter
                  name="Students"
                  data={studyHoursChartData}
                />

              </ScatterChart>

            </ResponsiveContainer>

          </div>


          <div className="correlation-summary">

            <strong>
              {analysis.correlation.study_hours_vs_average.toFixed(4)}
            </strong>

            <span>
              {analysis.correlation.direction} Correlation
            </span>

          </div>

        </section>



        {/* ================= PYTHON ANALYSIS ================= */}

        <section className="section">

          <div className="section-header">

            <h2>
              Python Performance Analysis
            </h2>

            <p>
              Students meeting different Python
              performance conditions
            </p>

          </div>


          <div className="python-grid">


            {/* Python > 80 */}

            <div className="analysis-card">

              <h3>
                Python &gt; 80
              </h3>

              <div className="analysis-number">

                {analysis.python_analysis.count_above_80}

              </div>

              <p>
                Students
              </p>

              <div className="student-list">

                {analysis.python_analysis.students_above_80.map(
                  (student) => (
                    <span key={student}>
                      {student}
                    </span>
                  )
                )}

              </div>

            </div>



            {/* AND condition */}

            <div className="analysis-card">

              <h3>
                Python &gt; 80 AND Attendance &gt; 90
              </h3>

              <div className="analysis-number">

                {
                  analysis.python_analysis
                    .python_above_80_and_attendance_above_90
                    .length
                }

              </div>

              <p>
                Students
              </p>

              <div className="student-list">

                {
                  analysis.python_analysis
                    .python_above_80_and_attendance_above_90
                    .map(
                      (student) => (
                        <span key={student}>
                          {student}
                        </span>
                      )
                    )
                }

              </div>

            </div>



            {/* OR condition */}

            <div className="analysis-card">

              <h3>
                Python &gt; 90 OR Attendance &gt; 95
              </h3>

              <div className="analysis-number">

                {
                  analysis.python_analysis
                    .python_above_90_or_attendance_above_95
                    .length
                }

              </div>

              <p>
                Students
              </p>

              <div className="student-list">

                {
                  analysis.python_analysis
                    .python_above_90_or_attendance_above_95
                    .map(
                      (student) => (
                        <span key={student}>
                          {student}
                        </span>
                      )
                    )
                }

              </div>

            </div>


          </div>

        </section>



        {/* ================= STUDENT TABLE ================= */}

        <section className="section">

          <div className="section-header">

            <h2>
              Student Details
            </h2>

            <p>
              Individual student performance
            </p>

          </div>


          <div className="table-container">

            <table>

              <thead>

                <tr>

                  <th>
                    Student ID
                  </th>

                  <th>
                    Average Score
                  </th>

                  <th>
                    Performance
                  </th>

                </tr>

              </thead>


              <tbody>

                {analysis.student_performance.map(
                  (student) => (

                    <tr
                      key={student.student_id}
                    >

                      <td>
                        {student.student_id}
                      </td>

                      <td>
                        {student.average.toFixed(2)}
                      </td>

                      <td>

                        <span
                          className={`performance ${getPerformanceLevel(
                            student.average
                          )
                            .toLowerCase()
                            .replaceAll(' ', '-')}`}
                        >

                          {getPerformanceLevel(
                            student.average
                          )}

                        </span>

                      </td>

                    </tr>

                  )
                )}

              </tbody>

            </table>

          </div>

        </section>



        {/* ================= PERFORMERS ================= */}

        <section className="performers-grid">


          <div className="performer-card">

            <p>
              🏆 Highest Performer
            </p>

            <h2>
              Student {analysis.highest_performer.student_id}
            </h2>

            <span>
              Average Score:{' '}
              {analysis.highest_performer.average.toFixed(2)}
            </span>

          </div>


          <div className="performer-card">

            <p>
              📉 Lowest Performer
            </p>

            <h2>
              Student {analysis.lowest_performer.student_id}
            </h2>

            <span>
              Average Score:{' '}
              {analysis.lowest_performer.average.toFixed(2)}
            </span>

          </div>


        </section>



        {/* ================= OUTLIERS ================= */}

        <section className="section">

          <h2>
            Outlier Analysis
          </h2>


          <div className="outlier-result">

            <strong>
              {analysis.outliers.total}
            </strong>

            <span>
              Potential outliers detected
            </span>

          </div>

        </section>


      </main>

    </div>

  )

}


export default App