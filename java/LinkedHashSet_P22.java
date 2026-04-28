import java.util.*;

public class LinkedHashSet_P22 {
    public static void main(String[] args) {
        Set<String> set = new LinkedHashSet<>();
        Scanner sc = new Scanner(System.in);

        set.add(sc.next());
        set.add(sc.next());

        System.out.println(set);
    }
}