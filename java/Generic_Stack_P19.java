import java.util.*;

class Stack<T> {
    ArrayList<T> list = new ArrayList<>();

    void push(T x) { list.add(x); }

    void pop() {
        if (list.size() > 0)
            list.remove(list.size() - 1);
    }

    public String toString() { return list.toString(); }
}

public class Generic_Stack_P19 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Stack<Integer> s = new Stack<>();

        for (int i = 0; i < 5; i++)
            s.push(sc.nextInt());

        System.out.println(s);
        s.pop();
        System.out.println(s);
    }
}