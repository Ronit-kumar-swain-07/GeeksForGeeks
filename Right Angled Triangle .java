/*
Right Angle Triangle

Given an integer n. Write a program to print the Right-angle triangle wall. The length of perpendicular and base is n. 
Note: Print exactly single " " after "*". Print a new line after printing the triangle.

Example:

Input: n = 4
Output:
* 
* * 
* * * 
* * * * 
Explanation: Length of perpendicular and base of triangle is 4 .

Input: n = 3
Output:
* 
* * 
* * * 
Explanation: Length of perpendicular and base of triangle is 3 .

Constraints:
1 ≤ n ≤ 10

Expected Complexities
Time Complexity: O(n^2)
Auxiliary Space: O(1)
*/

//Code

//Solution.java
import java.util.Scanner;

public class Solution {
    public static void solve() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = n; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}