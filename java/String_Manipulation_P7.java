import java.util.*;

class Word {
    String s;

    Word() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter string: ");
        s = sc.nextLine();
    }

    void operations() {
        System.out.println("Lower: " + s.toLowerCase());
        System.out.println("Upper: " + s.toUpperCase());
        System.out.println("Length: " + s.length());
        System.out.println("Substring(2): " + s.substring(2));
        System.out.println("Trim: " + s.trim());
        System.out.println("Index of o: " + s.indexOf('o'));
        System.out.println("Concat: " + s.concat("CR7"));
    }
}

public class String_Manipulation_P7 {
    public static void main(String[] args) {
        Word w = new Word();
        w.operations();
    }
}