import java.util.Scanner;
class Demo {
    void convert(double b[])
    {
        int c[]=new int[b.length];
        for (int i = 0; i < b.length; i++)
        {
            c[i]=(int)b[i];
        }
        for (int i = 0; i < b.length; i++)
        {
            System.out.println(c[i]);
        }
    }
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        double a[]=new double[10];
        System.out.println("Enter 10 double values");
        for(int i=0;i<10;i++) { a[i]=sc.nextDouble();
        }
        Demo d=new Demo(); d.convert(a); } }
