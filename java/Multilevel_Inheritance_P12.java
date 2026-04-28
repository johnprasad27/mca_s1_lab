import java.util.*;

class Person {
    String name, gender, address;
    int age;

    Person() {
        Scanner sc = new Scanner(System.in);
        name = sc.next();
        gender = sc.next();
        address = sc.next();
        age = sc.nextInt();
    }
}

class Emp extends Person {
    int empId;
    String company, qualification;
    double salary;

    Emp() {
        Scanner sc = new Scanner(System.in);
        empId = sc.nextInt();
        company = sc.next();
        qualification = sc.next();
        salary = sc.nextDouble();
    }
}

class TeacherM extends Emp {
    String subject, dept;
    int teacherId;

    TeacherM() {
        Scanner sc = new Scanner(System.in);
        subject = sc.next();
        dept = sc.next();
        teacherId = sc.nextInt();
    }

    void display() {
        System.out.println(name + " " + dept + " " + subject);
    }
}

public class Multilevel_Inheritance_P12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        TeacherM t[] = new TeacherM[n];

        for (int i = 0; i < n; i++)
            t[i] = new TeacherM();

        for (TeacherM x : t)
            x.display();
    }
}