import java.util.*;

class Table5 extends Thread {
    public void run() {
        for (int i = 1; i <= 10; i++)
            System.out.println(i * 5);
    }
}

class PrimeT extends Thread {
    int n;

    PrimeT(int n) { this.n = n; }

    public void run() {
        for (int i = 2; i <= n; i++) {
            boolean p = true;
            for (int j = 2; j <= i / 2; j++)
                if (i % j == 0) p = false;
            if (p) System.out.println(i);
        }
    }
}

public class Thread_Class_P17 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Table5 t1 = new Table5();
        PrimeT t2 = new PrimeT(sc.nextInt());

        t1.start();
        t2.start();
    }
}