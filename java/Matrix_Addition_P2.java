import java.util.*;

class AddMatrix {
    int n, m;
    int[][] matrix;

    AddMatrix(int x) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of matrix " + x + ": ");
        n = sc.nextInt();
        m = sc.nextInt();

        matrix = new int[n][m];

        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                matrix[i][j] = sc.nextInt();
    }

    void add(AddMatrix b) {
        if (n != b.n || m != b.m) {
            System.out.println("Addition not possible");
            return;
        }

        System.out.println("Sum:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                System.out.print((matrix[i][j] + b.matrix[i][j]) + " ");
            System.out.println();
        }
    }
}

public class Matrix_Addition_P2 {
    public static void main(String[] args) {
        AddMatrix a = new AddMatrix(1);
        AddMatrix b = new AddMatrix(2);
        a.add(b);
    }
}