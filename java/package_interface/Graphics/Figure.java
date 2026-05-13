package Graphics;

public interface Figure {

    public static class Circle {

        double radius;

        public Circle(double radius) {
            this.radius = radius;
        }

        public void area() {
            System.out.println("Area of Circle = " + (3.14 * radius * radius));
        }
    }

    public static class Rectangle {

        double length, breadth;

        public Rectangle(double length, double breadth) {
            this.length = length;
            this.breadth = breadth;
        }

        public void area() {
            System.out.println("Area of Rectangle = " + (length * breadth));
        }
    }

    public static class Square {

        double side;

        public Square(double side) {
            this.side = side;
        }

        public void area() {
            System.out.println("Area of Square = " + (side * side));
        }
    }

    public static class Triangle {

        double breadth, height;

        public Triangle(double breadth, double height) {
            this.breadth = breadth;
            this.height = height;
        }

        public void area() {
            System.out.println("Area of Triangle = " + (0.5 * breadth * height));
        }
    }
}