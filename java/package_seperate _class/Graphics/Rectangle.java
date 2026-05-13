package Graphics;

public class Rectangle implements Figure {

    double length, breadth;

    public Rectangle(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    public void area() {
        System.out.println("Area of Rectangle = " + (length * breadth));
    }
}