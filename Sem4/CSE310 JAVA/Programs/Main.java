import java.util.Scanner;
class Main
{
    public static void main(String[] args) {//calling method
        int[] a; //declaration
        a=new int[10];

        Scanner sc=new Scanner(System.in);
        System.out.println("Enter 10 numbers");
        for(int i=0;i<10;i++)
        {
            a[i] =sc.nextInt();
        }
//String s= Arrays.toString(a);
//System.out.println(s);
        boolean flag=false;
        for(int i=0;i<10;i++)
        {
            if(a[i]==46){
                flag=true;
            }
        }
        if (flag==true){
            System.out.println("Found");
        } else {
            System.out.println("Not found");
        }
    }

}