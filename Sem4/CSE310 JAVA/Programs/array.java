import java.util.Scanner;

public class array
{
    public static void main (String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int max = 0;
        //int sum = 0;
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
            //sum = sum+arr[i];
        }

        for(int i=0;i<n;i++){
            if (max<arr[i]){
                max=arr[i];
            }
        }
        System.out.println(max);
        int min = 99999;
        for(int i=0;i<n;i++){
            if (min>arr[i]){
                min=arr[i];
            }
        }
        System.out.println(min);
    }
}
