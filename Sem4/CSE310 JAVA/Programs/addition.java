import java.util.Scanner;

public class addition {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        float b = sc.nextFloat();
        System.out.println("Int sum : "+(a+(int)b));
        System.out.println(("Float sum : ")+((float)a+b));
    }
}

