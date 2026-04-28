import java.util.*;

interface Area {
    void area();
}

class Rectangle implements Area {
    int l, b;

    Rectangle(int l, int b) {
        this.l = l;
        this.b = b;
    }

    public void area() {
        System.out.println("Area: " + (l * b));
    }
}

public class Interface_P13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Rectangle r = new Rectangle(sc.nextInt(), sc.nextInt());
        r.area();
    }
}   