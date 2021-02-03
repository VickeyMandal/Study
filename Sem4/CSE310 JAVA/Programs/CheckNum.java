import java.util.Scanner;
public class CheckNum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println("Digit to check : ");
        int c = sc.nextInt();
        boolean flag = false;
        while(n>0){
            int r = n%10;
            if(r==c)
            {
                System.out.println("Present");
                flag = true;
                break;
            }
            n = n/10;
        }
        if(flag==false){
            System.out.println("Absent");
        }
    }
}
