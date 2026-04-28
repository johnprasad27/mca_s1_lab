import java.util.*;

class CPU {
    int price;

    class Processor {
        int cores;
        String manufacturer;

        Processor() {
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter cores: ");
            cores = sc.nextInt();
            System.out.print("Enter manufacturer: ");
            manufacturer = sc.next();
        }
    }

    static class RAM {
        int memory;
        String manufacturer;

        RAM() {
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter memory: ");
            memory = sc.nextInt();
            System.out.print("Enter manufacturer: ");
            manufacturer = sc.next();
        }
    }
}

public class Inner_Class_CPU_P5 {
    public static void main(String[] args) {
        CPU c = new CPU();
        CPU.Processor p = c.new Processor();
        CPU.RAM r = new CPU.RAM();

        c.price = 2500 + p.cores * 20 + r.memory * 15;

        System.out.println("CPU Price: " + c.price);
    }
}