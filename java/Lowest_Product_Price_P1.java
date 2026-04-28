import java.util.*;

class Product {
    String pcode, pname;
    int price;

    void details(int n) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter product code for item " + n + ": ");
        pcode = sc.next();
        System.out.print("Enter product name: ");
        pname = sc.next();
        System.out.print("Enter price: ");
        price = sc.nextInt();
    }

    void lowest(Product a, Product b) {
        if (price < a.price && price < b.price)
            System.out.println("Product " + pname + " has lowest price");
        else if (a.price < b.price)
            System.out.println("Product " + a.pname + " has lowest price");
        else
            System.out.println("Product " + b.pname + " has lowest price");
    }
}

public class Lowest_Product_Price_P1 {
    public static void main(String[] args) {
        Product p1 = new Product();
        Product p2 = new Product();
        Product p3 = new Product();

        p1.details(1);
        p2.details(2);
        p3.details(3);

        p1.lowest(p2, p3);
    }
}