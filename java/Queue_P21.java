import java.util.*;

public class Queue_P21 {
    public static void main(String[] args) {
        PriorityQueue<String> q = new PriorityQueue<>();
        Scanner sc = new Scanner(System.in);

        q.add(sc.next());
        q.add(sc.next());

        System.out.println(q);
    }
}