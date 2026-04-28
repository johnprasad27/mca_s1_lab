import java.util.*;

class Employee {
    int eNo;
    String eName;
    double salary;

    Employee(int n) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter details for employee " + n);
        eNo = sc.nextInt();
        eName = sc.next();
        salary = sc.nextDouble();
    }
}

public class Array_of_Objects_P8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Employee e[] = new Employee[n];

        for (int i = 0; i < n; i++)
            e[i] = new Employee(i + 1);

        int key = sc.nextInt();

        boolean found = false;
        for (Employee emp : e) {
            if (emp.eNo == key) {
                System.out.println(emp.eName + " " + emp.salary);
                found = true;
            }
        }

        if (!found)
            System.out.println("Employee not found");
    }
}