import java.util.*;

class Shape {
    void area(double r) {
        System.out.println("Circle: " + (3.14 * r * r));
    }

    void area(float s) {
        System.out.println("Square: " + (s * s));
    }

    void area(double l, double b) {
        System.out.println("Rectangle: " + (l * b));
    }

    void area(float b, float h) {
        System.out.println("Triangle: " + (0.5 * b * h));
    }
}

public class Function_Overloading_P10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Shape s = new Shape();

        s.area(sc.nextDouble());
        s.area(sc.nextFloat());

        double l = sc.nextDouble();
        double b = sc.nextDouble();
        s.area(l, b);

        float b1 = sc.nextFloat();
        float h1 = sc.nextFloat();
        s.area(b1, h1);
    }
}