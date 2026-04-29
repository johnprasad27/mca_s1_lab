import java.io.*;
import java.util.*;

public class File_Write_Read_P26 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        String fileName = sc.nextLine();

        FileOutputStream fos = new FileOutputStream(fileName);

        String text = sc.nextLine();
        fos.write(text.getBytes());
        fos.close();

        FileInputStream fis = new FileInputStream(fileName);

        byte[] b = new byte[fis.available()];
        fis.read(b);
        fis.close();

        System.out.println(new String(b));
    }
}