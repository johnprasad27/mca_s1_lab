import java.io.File;
import java.util.Scanner;

public class Directory_Listing_P25 {

    static void listFiles(File dir) {
        File[] files = dir.listFiles();

        if (files != null) {
            for (File f : files) {
                System.out.println(f.getName());
                if (f.isDirectory())
                    listFiles(f);
            }
        }
    }

    static void searchFile(File dir, String name) {
        File[] files = dir.listFiles();

        if (files != null) {
            for (File f : files) {
                if (f.isFile() && f.getName().equals(name)) {
                    System.out.println("Found: " + f.getAbsolutePath());
                    return;
                }
                if (f.isDirectory())
                    searchFile(f, name);
            }
        }
        System.out.println("File not found");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String path = sc.nextLine();
        File dir = new File(path);

        if (dir.exists() && dir.isDirectory()) {
            listFiles(dir);

            String name = sc.nextLine();
            searchFile(dir, name);
        } else {
            System.out.println("Invalid directory");
        }
    }
}