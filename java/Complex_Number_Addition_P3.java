import java.util.*;

class Complex {
    int x, y;

    void input(int n) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter real part of number " + n + ": ");
        x = sc.nextInt();
        System.out.print("Enter imaginary part: ");
        y = sc.nextInt();
    }

    void add(Complex b) {
        System.out.println("(" + x + "+i" + y + ") + (" + b.x + "+i" + b.y + ") = "
                + (x + b.x) + "+i" + (y + b.y));
    }
}

public class Complex_Number_Addition_P3 {
    public static void main(String[] args) {
        Complex a = new Complex();
        Complex b = new Complex();

        a.input(1);
        b.input(2);

        a.add(b);
    }
}