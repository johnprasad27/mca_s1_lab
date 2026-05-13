package Graphics;

public class Square implements Figure {

    double side;

    public Square(double side) {
        this.side = side;
    }

    public void area() {
        System.out.println("Area of Square = " + (side * side));
    }
}