import java.util.*;

class Fib implements Runnable {
    int n;

    Fib(int n) { this.n = n; }

    public void run() {
        int a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            System.out.println(a);
            int c = a + b;
            a = b;
            b = c;
        }
    }
}

class EvenR implements Runnable {
    int s, e;

    EvenR(int s, int e) { this.s = s; this.e = e; }

    public void run() {
        for (int i = s; i <= e; i++)
            if (i % 2 == 0)
                System.out.println(i);
    }
}

public class Runnable_Interface_P18 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Thread t1 = new Thread(new Fib(sc.nextInt()));
        Thread t2 = new Thread(new EvenR(sc.nextInt(), sc.nextInt()));

        t1.start();
        t2.start();
    }
}