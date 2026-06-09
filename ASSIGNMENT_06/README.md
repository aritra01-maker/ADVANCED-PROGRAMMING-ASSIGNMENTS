# Assignment 06 - Student Performance Analyzer in Java

## Question
Develop a student performance analyzer in Java.

Each student has:
- \id\ (int) â€” don't include CSB prefix
- \
ame\ (String)
- \courses\ (List<String>)
- \scores\ (Map<String, Integer>) â€” key = course, value = marks

### Required Methods:
\\\java
List<Student> getTopNStudents(List<Student> students, int n);
Map<String, Double> getAverageScorePerCourse(List<Student> students);
Set<String> getAllUniqueCourses(List<Student> students);
\\\

### Must Use:
1. ArrayList, HashMap, and HashSet
2. Streams for aggregation and filtering
3. Sort students by average score (descending)
4. Comparator
5. Handle missing course scores using getOrDefault
6. Type safety using generics

### Complexity Analysis:
1. What is the time complexity of computing course averages?
2. What is the complexity of sorting top N students?

## Language
Java

## Files
- \Student.java\
- \StudentAnalyzer.java\
