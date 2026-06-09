import { useState } from "react"

function AddStudentForm({ addStudent }) {
  const [id, setId] = useState("")
  const [name, setName] = useState("")
  const [courses, setCourses] = useState("")
  const [gpa, setGpa] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()

    const courseSet = new Set(
      courses.split(",").map(course => course.trim())
    )

    const newStudent = {
      id: Number(id),
      name,
      enrolledCourses: courseSet,
      gpa: Number(gpa)
    }

    addStudent(newStudent)

    setId("")
    setName("")
    setCourses("")
    setGpa("")
  }

  return (
    <div className="card">
      <h3>Add Student</h3>
      <form onSubmit={handleSubmit}>
        <input placeholder="ID" value={id} onChange={e => setId(e.target.value)} required />
        <input placeholder="Name" value={name} onChange={e => setName(e.target.value)} required />
        <input placeholder="Courses (comma separated)" value={courses} onChange={e => setCourses(e.target.value)} required />
        <input placeholder="GPA" value={gpa} onChange={e => setGpa(e.target.value)} required />
        <button type="submit">Add Student</button>
      </form>
    </div>
  )
}

export default AddStudentForm