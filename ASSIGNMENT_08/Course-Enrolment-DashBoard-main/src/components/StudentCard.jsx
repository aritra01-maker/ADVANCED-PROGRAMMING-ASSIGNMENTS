function StudentCard({ student, removeStudent }) {
  return (
    <div className="student-card">
      <h4>{student.name}</h4>
      <p>GPA: {student.gpa}</p>
      <p>Courses: {Array.from(student.enrolledCourses).join(", ")}</p>
      <button onClick={() => removeStudent(student.id)}>
        Remove
      </button>
    </div>
  )
}

export default StudentCard