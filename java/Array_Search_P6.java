import java.util.*;

class ArraySearch {
    int arr[], size;

    ArraySearch(int n) {
        Scanner sc = new Scanner(System.in);
        size = n;
        arr = new int[n];

        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
    }

    void search(int key) {
        boolean found = false;

        for (int i = 0; i < size; i++)
            if (arr[i] == key)
                found = true;

        if (found)
            System.out.println("Element found");
        else
            System.out.println("Element not found");
    }
}

public class Array_Search_P6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ArraySearch a = new ArraySearch(n);

        int key = sc.nextInt();
        a.search(key);
    }
}