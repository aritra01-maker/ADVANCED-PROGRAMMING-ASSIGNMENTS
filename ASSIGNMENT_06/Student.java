import java.util.*;

public class Student {

    private int id;
    private String name;
    private List<String> courses;
    private Map<String, Integer> scores;

    public Student(int id, String name,
                   List<String> courses,
                   Map<String, Integer> scores) {
        this.id = id;
        this.name = name;
        this.courses = courses;
        this.scores = scores;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public List<String> getCourses() {
        return courses;
    }

    public Map<String, Integer> getScores() {
        return scores;
    }

    // Calculate average marks of this student
    public double getAverageScore() {
        if (scores.isEmpty())
            return 0.0;

        return scores.values()
                .stream()
                .mapToInt(Integer::intValue)
                .average()
                .orElse(0.0);
    }

    @Override
    public String toString() {
        return "ID=" + id +
               ", Name=" + name +
               ", Avg=" + String.format("%.2f", getAverageScore());
    }
}