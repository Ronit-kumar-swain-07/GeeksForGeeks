// Given an integer n,  write a program to print the square wall of size n using a single loop and string multiplication. 

// Code

import java.util.*;

class Solution {
    public static void main(String args[]) {
        // Your Code Here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // for(int i = 0; i<n; i++) {
        //     for(int j = 0; j<n;j++) {
        //         System.out.print("* ");
        //     }
        //     System.out.println();
        // }

        String row = "* ".repeat(n);   

        for (int i = 0; i < n; i++) {
            System.out.println(row);
        }

        sc.close();
    }
}