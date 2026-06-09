function CourseFilter({ uniqueCourses, setFilterCourse }) {
  return (
    <div className="card">
      <h3>Filter by Course</h3>
      <select onChange={(e) => setFilterCourse(e.target.value)}>
        <option value="">All Courses</option>
        {Array.from(uniqueCourses).map(course => (
          <option key={course} value={course}>
            {course}
          </option>
        ))}
      </select>
    </div>
  )
}

export default CourseFilter