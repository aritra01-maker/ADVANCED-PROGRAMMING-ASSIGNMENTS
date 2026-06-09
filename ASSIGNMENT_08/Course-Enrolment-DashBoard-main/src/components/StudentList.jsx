import StudentCard from "./StudentCard"

function StudentList({ students, removeStudent }) {
  return (
    <div className="card">
      <h3>Students</h3>
      {students.length === 0 ? (
        <p>No students found</p>
      ) : (
        students.map(student => (
          <StudentCard
            key={student.id}
            student={student}
            removeStudent={removeStudent}
          />
        ))
      )}
    </div>
  )
}

export default StudentList