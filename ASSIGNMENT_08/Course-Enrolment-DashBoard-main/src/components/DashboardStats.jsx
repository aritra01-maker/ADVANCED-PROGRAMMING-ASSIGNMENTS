function DashboardStats({ stats }) {
  return (
    <div className="card stats">
      <h3>Statistics</h3>
      <p>Average GPA: {stats.avg}</p>
      <p>Highest GPA: {stats.max}</p>
      <p>Lowest GPA: {stats.min}</p>
    </div>
  )
}

export default DashboardStats