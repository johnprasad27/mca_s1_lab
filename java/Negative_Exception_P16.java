import java.util.*;

class Negative extends RuntimeException {
    Negative(String s) { super(s); }
}

public class Negative_Exception_P16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int sum = 0;

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            if (x < 0)
                throw new Negative("Negative not allowed");
            sum += x;
        }

        System.out.println("Average: " + (sum / n));
    }
}