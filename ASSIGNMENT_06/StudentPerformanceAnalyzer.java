import java.util.*;
import java.util.stream.*;

public class StudentPerformanceAnalyzer {

    // 1️ Top N students sorted by average (descending)
    public static List<Student> getTopNStudents(List<Student> students, int n) {

        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore)
                        .reversed())
                .limit(n)
                .collect(Collectors.toList());
    }


    // 2️ Average score per course
    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {

        Map<String, Double> courseAverage = new HashMap<>();

        Set<String> allCourses = getAllUniqueCourses(students);

        for (String course : allCourses) {

            double avg = students.stream()
                    .mapToInt(s -> s.getScores().getOrDefault(course, 0))
                    .average()
                    .orElse(0.0);

            courseAverage.put(course, avg);
        }

        return courseAverage;
    }


    // 3️ All unique courses
    public static Set<String> getAllUniqueCourses(List<Student> students) {

        return students.stream()
                .flatMap(s -> s.getCourses().stream())
                .collect(Collectors.toCollection(HashSet::new));
    }
}