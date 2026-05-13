import Graphics.Figure;
import java.util.*;

public class GraphicsTest {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius: ");
        Figure.Circle c =
                new Figure.Circle(sc.nextDouble());
        c.area();

        System.out.print("Enter length and breadth: ");
        Figure.Rectangle r =
                new Figure.Rectangle(sc.nextDouble(), sc.nextDouble());
        r.area();

        System.out.print("Enter side: ");
        Figure.Square s =
                new Figure.Square(sc.nextDouble());
        s.area();

        System.out.print("Enter breadth and height: ");
        Figure.Triangle t =
                new Figure.Triangle(sc.nextDouble(), sc.nextDouble());
        t.area();
    }
}