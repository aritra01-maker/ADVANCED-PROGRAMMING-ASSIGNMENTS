import java.util.ArrayList;
import java.util.Scanner;

public class BookSearch {
    public static void main(String[] args) {

        ArrayList<String> books = new ArrayList<>();

        books.add("Introduction to Java");
        books.add("Data Structures in Java");
        books.add("Operating System Concepts");
        books.add("Database Management Systems");
        books.add("Computer Networks");

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word to search: ");
        String keyword = sc.nextLine().toLowerCase();

        System.out.println("\nBooks containing the word \"" + keyword + "\":");
        for (String book : books) {
            if (book.toLowerCase().contains(keyword)) {
                System.out.println(book);
            }
        }

        sc.close();
    }
}
