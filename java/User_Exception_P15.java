import java.util.*;

class NameException extends RuntimeException {
    NameException(String s) { super(s); }
}

class PassException extends RuntimeException {
    PassException(String s) { super(s); }
}

class User {
    String name, pass;

    User(String n, String p) {
        name = n;
        pass = p;
    }

    void login(String n, String p) {
        if (name.equals(n) && pass.equals(p))
            System.out.println("Login success");
        else
            throw new PassException("Invalid login");
    }
}

public class User_Exception_P15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String name = sc.next();
        String pass = sc.next();

        User u = new User(name, pass);

        String n = sc.next();
        String p = sc.next();

        u.login(n, p);
    }
}