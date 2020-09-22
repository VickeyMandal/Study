import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Solution {


    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();

         for(int i = 0;i<=n;i++){
            for(int j=1;j<=i-1;j++)
            {
                System.out.print("#");
            }
            System.out.println("@");
        }
        scanner.close();
    }
}
