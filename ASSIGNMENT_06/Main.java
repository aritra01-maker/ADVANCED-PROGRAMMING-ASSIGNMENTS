import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        System.out.print("Enter number of students: ");
        int n = sc.nextInt();

        System.out.print("Enter value of N for Top N students: ");
        int topN = sc.nextInt();

        List<Student> students = new ArrayList<>();

        List<String> availableCourses =
                Arrays.asList("Math", "Physics", "Java", "DSA", "DBMS");

        for (int i = 0; i < n; i++) {

            int roll = 1000 + random.nextInt(9000); // Random 4-digit ID
            String name = "Student_" + (i + 1);

            // Randomly select 2–5 courses
            Collections.shuffle(availableCourses);
            int numberOfCourses = 2 + random.nextInt(4);

            List<String> selectedCourses =
                    new ArrayList<>(availableCourses.subList(0, numberOfCourses));

            Map<String, Integer> scores = new HashMap<>();

            for (String course : selectedCourses) {
                scores.put(course, 40 + random.nextInt(61)); // Marks 40–100
            }

            students.add(new Student(
                    roll,
                    name,
                    selectedCourses,
                    scores
            ));
        }

        // 🔹 Display all students
        System.out.println("\nAll Students:");
        students.forEach(System.out::println);

        // 🔹 Top N Students
        long startSort = System.nanoTime();

        List<Student> topStudents =
                StudentPerformanceAnalyzer.getTopNStudents(students, topN);

        long endSort = System.nanoTime();

        System.out.println("\nTop " + topN + " Students:");
        topStudents.forEach(System.out::println);

        System.out.println("Sorting Time: " +
                (endSort - startSort) + " ns");


        // 🔹 Course Averages
        long startAvg = System.nanoTime();

        Map<String, Double> averages =
                StudentPerformanceAnalyzer.getAverageScorePerCourse(students);

        long endAvg = System.nanoTime();

        System.out.println("\nCourse Averages:");
        averages.forEach((course, avg) ->
                System.out.println(course + " : " +
                        String.format("%.2f", avg)));

        System.out.println("Average Computation Time: " +
                (endAvg - startAvg) + " ns");


        // 🔹 Unique Courses
        System.out.println("\nUnique Courses:");
        Set<String> courses =
                StudentPerformanceAnalyzer.getAllUniqueCourses(students);

        courses.forEach(System.out::println);

        sc.close();
    }
}