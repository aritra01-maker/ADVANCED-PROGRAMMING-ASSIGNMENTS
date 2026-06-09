import { useState, useMemo, useEffect } from "react"

export default function useStudents() {

  // Load from localStorage initially
  const [studentsMap, setStudentsMap] = useState(() => {
    const stored = localStorage.getItem("students")
    if (!stored) return new Map()

    const parsed = JSON.parse(stored)

    // Convert back to Map and Set
    const map = new Map()
    parsed.forEach(student => {
      map.set(student.id, {
        ...student,
        enrolledCourses: new Set(student.enrolledCourses)
      })
    })

    return map
  })

  const [filterCourse, setFilterCourse] = useState("")

  // Save to localStorage whenever studentsMap changes
  useEffect(() => {
    const array = Array.from(studentsMap.values()).map(student => ({
      ...student,
      enrolledCourses: Array.from(student.enrolledCourses)
    }))
    localStorage.setItem("students", JSON.stringify(array))
  }, [studentsMap])

  const studentsArray = useMemo(() => {
    return Array.from(studentsMap.values())
  }, [studentsMap])

  const addStudent = (student) => {
    setStudentsMap(prev => {
      const newMap = new Map(prev)
      newMap.set(student.id, student)
      return newMap
    })
  }

  const removeStudent = (id) => {
    setStudentsMap(prev => {
      const newMap = new Map(prev)
      newMap.delete(id)
      return newMap
    })
  }

  const sortedStudents = useMemo(() => {
    return [...studentsArray].sort((a, b) => b.gpa - a.gpa)
  }, [studentsArray])

  const filteredStudents = useMemo(() => {
    if (!filterCourse) return sortedStudents
    return sortedStudents.filter(student =>
      student.enrolledCourses.has(filterCourse)
    )
  }, [sortedStudents, filterCourse])

  const uniqueCourses = useMemo(() => {
    return studentsArray.reduce((acc, student) => {
      student.enrolledCourses.forEach(course => acc.add(course))
      return acc
    }, new Set())
  }, [studentsArray])

  const stats = useMemo(() => {
    if (studentsArray.length === 0)
      return { avg: 0, max: 0, min: 0 }

    const total = studentsArray.reduce((sum, s) => sum + s.gpa, 0)
    const max = Math.max(...studentsArray.map(s => s.gpa))
    const min = Math.min(...studentsArray.map(s => s.gpa))

    return {
      avg: (total / studentsArray.length).toFixed(2),
      max,
      min
    }
  }, [studentsArray])

  return {
    filteredStudents,
    addStudent,
    removeStudent,
    uniqueCourses,
    setFilterCourse,
    stats
  }
}