import java.util.*;

class nameexception extends RuntimeException {

    nameexception(String msg) {
        super(msg);
    }
}

class passexception extends RuntimeException {

    passexception(String msg) {
        super(msg);
    }
}

class user {

    String name, password;

    user(String name, String password) {
        this.name = name;
        this.password = password;
    }

    void login(String uname, String pass) {

        if (name.equals(uname) && password.equals(pass)) {
            System.out.println("Login Successful");
        } else {
            throw new RuntimeException("Invalid username or password");
        }
    }
}

public class UserAuthentication {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter username: ");
        String name = sc.next();

        for (int i = 0; i < name.length(); i++) {

            if (!Character.isLetter(name.charAt(i))) {
                throw new nameexception("Invalid Name");
            }
        }

        System.out.print("Enter password: ");
        String password = sc.next();

        if (password.length() < 8) {
            throw new passexception("Password must contain minimum 8 characters");
        }

        boolean digit = false;

        for (int i = 0; i < password.length(); i++) {

            if (Character.isDigit(password.charAt(i))) {
                digit = true;
                break;
            }
        }

        if (!digit) {
            throw new passexception("Password must contain atleast 1 digit");
        }

        user u = new user(name, password);

        System.out.print("Enter login username: ");
        String uname = sc.next();

        System.out.print("Enter login password: ");
        String pass = sc.next();

        u.login(uname, pass);
    }
}