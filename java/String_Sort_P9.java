import java.util.*;

class SortString {
    String s[];
    int size;

    SortString() {
        Scanner sc = new Scanner(System.in);
        size = sc.nextInt();
        s = new String[size];

        for (int i = 0; i < size; i++)
            s[i] = sc.next();
    }

    void sort() {
        for (int i = 0; i < size; i++)
            for (int j = 0; j < size - i - 1; j++)
                if (s[j].compareTo(s[j + 1]) > 0) {
                    String temp = s[j];
                    s[j] = s[j + 1];
                    s[j + 1] = temp;
                }
    }

    void display() {
        for (String str : s)
            System.out.print(str + " ");
    }
}

public class String_Sort_P9 {
    public static void main(String[] args) {
        SortString s = new SortString();
        s.display();
        s.sort();
        System.out.println("\nSorted:");
        s.display();
    }
}