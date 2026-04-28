import java.util.*;

class Symmetric {
    int n, m;
    int[][] matrix;

    Symmetric() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size: ");
        n = sc.nextInt();
        m = sc.nextInt();

        matrix = new int[n][m];

        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                matrix[i][j] = sc.nextInt();
    }

    void check() {
        boolean flag = true;

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (matrix[i][j] != matrix[j][i])
                    flag = false;

        if (flag)
            System.out.println("Matrix is symmetric");
        else
            System.out.println("Matrix is not symmetric");
    }
}

public class Symmetric_Matrix_P4 {
    public static void main(String[] args) {
        Symmetric s = new Symmetric();
        s.check();
    }
}