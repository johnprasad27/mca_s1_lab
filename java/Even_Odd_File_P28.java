import java.io.*;

public class Even_Odd_File_P28 {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputFile = br.readLine();

        BufferedReader fileReader = new BufferedReader(new FileReader(inputFile));
        BufferedWriter evenWriter = new BufferedWriter(new FileWriter("even.txt"));
        BufferedWriter oddWriter = new BufferedWriter(new FileWriter("odd.txt"));

        String line;

        while ((line = fileReader.readLine()) != null) {
            int num = Integer.parseInt(line);

            if (num % 2 == 0) {
                evenWriter.write(line);
                evenWriter.newLine();
            } else {
                oddWriter.write(line);
                oddWriter.newLine();
            }
        }

        fileReader.close();
        evenWriter.close();
        oddWriter.close();

        System.out.println("Separated successfully");
    }
}