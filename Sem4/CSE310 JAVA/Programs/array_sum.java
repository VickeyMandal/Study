import java.util.Scanner;

public class array_sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println("Initial array");
        for (int i=0;i<n;i++){
            System.out.print(arr[i]);
        }
        arr[2] = 0;
        for (int i=2;i<n-1;i++){
            arr[i]=arr[i+1];
        }




        System.out.println();
        System.out.println("After deletion array");
        for (int i=0;i<n-1;i++){
            System.out.print(arr[i]);
        }






    }
}
