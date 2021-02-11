
import java.util.Scanner;

class twodarray
{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int marks[][]=new int[3][];
        marks[0]=new int[5];
        marks[1]=new int[2];
        marks[2]=new int[1];
        for(int i=0;i<3;i++)
        {
            System.out.println("Enter marks for student "+(i+1));
            for(int j=0;j<marks[i].length;j++)
            {
                marks[i][j]=sc.nextInt();
            }
        }
        for(int i=0;i<3;i++)
        {
            int sum=0;
            for(int j=0;j<marks[i].length;j++)
            {
                sum=sum+marks[i][j];
            }
            System.out.println("Percentage obtained by student "+(i+1)+": "+((double)sum/(marks[i].length*100))*100);
        }


    }
}
