package Graphics;

public class Circle implements Figure {

    double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public void area() {
        System.out.println("Area of Circle = " + (3.14 * radius * radius));
    }
}