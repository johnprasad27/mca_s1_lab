import java.util.*;

class Employee {
    int empId;
    String name, address;
    double salary;

    Employee(int i) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter details of Teacher " + i);
        empId = sc.nextInt();
        name = sc.next();
        salary = sc.nextDouble();
        address = sc.next();
    }
}

class Teacher extends Employee {
    String dept;
    String subject[];
    int n;

    Teacher(int i) {
        super(i);
        Scanner sc = new Scanner(System.in);
        dept = sc.next();
        n = sc.nextInt();
        subject = new String[n];
        for (int j = 0; j < n; j++)
            subject[j] = sc.next();
    }

    void display() {
        System.out.println(empId + " " + name + " " + salary + " " + address + " " + dept);
        for (String s : subject)
            System.out.print(s + " ");
    }
}

public class Single_Inheritance_P11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Teacher t[] = new Teacher[n];

        for (int i = 0; i < n; i++)
            t[i] = new Teacher(i + 1);

        for (Teacher x : t) {
            x.display();
            System.out.println();
        }
    }
}