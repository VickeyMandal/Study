
import java.util.Scanner;

public class Discount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter section :- \n B M G W");
        String section = sc.next();
        section=section.toUpperCase();
        double totalCost,disc,finalCost;
        switch (section)
        {
            case ("B"):
                System.out.println("Enter total cost : ");
                totalCost=sc.nextInt();
                disc=totalCost*0.2;
                finalCost=totalCost-disc;
                System.out.println("Final Price : "+finalCost);
                break;
            case ("M"):
                System.out.println("Enter total cost : ");
                totalCost=sc.nextInt();
                disc=totalCost*0.3;
                finalCost=totalCost-disc;
                System.out.println("Final Price : "+finalCost);
                break;
            case ("G"):
                System.out.println("Enter total cost : ");
                totalCost=sc.nextInt();
                disc=totalCost*0.4;
                finalCost=totalCost-disc;
                System.out.println("Final Price : "+finalCost);
                break;
            case ("W"):
                System.out.println("Enter total cost : ");
                totalCost=sc.nextInt();
                disc=totalCost*0.45;
                finalCost=totalCost-disc;
                System.out.println("Final Price : "+finalCost);
                break;
            default:
                System.out.println("Invalid Section");

        }
    }
}
