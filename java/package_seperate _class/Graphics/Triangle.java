package Graphics;

public class Triangle implements Figure {

    double breadth, height;

    public Triangle(double breadth, double height) {
        this.breadth = breadth;
        this.height = height;
    }

    public void area() {
        System.out.println("Area of Triangle = " + (0.5 * breadth * height));
    }
}