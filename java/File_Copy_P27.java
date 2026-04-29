import java.io.*;

public class File_Copy_P27 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String src = br.readLine();
        String dest = br.readLine();

        InputStream in = new FileInputStream(src);
        OutputStream out = new FileOutputStream(dest);

        byte[] buffer = new byte[1024];
        int len;

        while ((len = in.read(buffer)) > 0)
            out.write(buffer, 0, len);

        in.close();
        out.close();

        System.out.println("Copied successfully");
    }
}