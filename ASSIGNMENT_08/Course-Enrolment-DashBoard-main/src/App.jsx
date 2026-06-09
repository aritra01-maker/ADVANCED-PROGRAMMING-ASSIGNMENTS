import useStudents from "./hooks/useStudents"
import AddStudentForm from "./components/AddStudentForm"
import StudentList from "./components/StudentList"
import CourseFilter from "./components/CourseFilter"
import DashboardStats from "./components/DashboardStats"
import "./styles/dashboard.css"

function App() {
  const {
    filteredStudents,
    addStudent,
    removeStudent,
    uniqueCourses,
    setFilterCourse,
    stats
  } = useStudents()

  return (
    <div className="container">
      <h1>📚 Course Enrollment Dashboard</h1>

      <DashboardStats stats={stats} />
      <AddStudentForm addStudent={addStudent} />
      <CourseFilter 
        uniqueCourses={uniqueCourses}
        setFilterCourse={setFilterCourse}
      />
      <StudentList 
        students={filteredStudents}
        removeStudent={removeStudent}
      />
    </div>
  )
}

export default App