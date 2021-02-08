import java.util.Scanner;

class Main {
    int[] convert(double b[]) {
        int c[]=new int[b.length];
        for (int i = 0; i < b.length; i++) {
            c[i]=(int)b[i];
        }
        return c;
    }
    public static void main(String[] args) {//double array to int
        Scanner sc=new Scanner(System.in);
        double a[]=new double[10];
        System.out.println("Enter 10 double values");
        for(int i=0;i<10;i++)
        {
            a[i]=sc.nextDouble();
        }
        Main d=new Main();
        int[] r=d.convert(a);
        for (int i = 0; i < r.length; i++) {
            System.out.println(r[i]);
        }
    }
}