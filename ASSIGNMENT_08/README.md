# Assignment 08 - Course Enrollment Dashboard in React

## Question
Develop a course enrollment dashboard in ReactJS.

Each student:
\\\js
{
  id: number,
  name: string,
  enrolledCourses: Set<string>,
  gpa: number
}
\\\

### Features:
- Add new student
- Remove student by ID
- Display students sorted by GPA (descending)
- Display all unique courses across students
- Filter students enrolled in a specific course

### Must Use:
- useState
- Map internally for id-to-student mapping
- Set for course uniqueness
- map, filter, and reduce
- No direct state mutation
- Spread operator for updates
- Convert Set to array before rendering

### Complexity Analysis:
- Time complexity of filtering students by course

## Language
JavaScript / React

## Files
- \App.js\ or \EnrollmentDashboard.jsx\
