import Graphics.*;
import java.util.*;

public class GraphicsTest {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius: ");
        Circle c = new Circle(sc.nextDouble());
        c.area();

        System.out.print("Enter length and breadth: ");
        Rectangle r = new Rectangle(sc.nextDouble(), sc.nextDouble());
        r.area();

        System.out.print("Enter side: ");
        Square s = new Square(sc.nextDouble());
        s.area();

        System.out.print("Enter breadth and height: ");
        Triangle t = new Triangle(sc.nextDouble(), sc.nextDouble());
        t.area();
    }
}