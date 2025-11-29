/*
Inverted Right AngleTriangle

Given an integer S. Write a program to print the Inverted "Right angle triangle" wall. 
The length of the perpendicular and base is S.
Note: There is exactly one " " after a "*". Print a new line after printing the triangle.

Examples:

Input: S = 4
Output:
* * * * 
* * * 
* * 
*
Explanation: Length of perpendicular and base of triangle is 4 .

Input: S = 3
Output:
* * * 
* * 
*
Explanation: Length of perpendicular and base of triangle is 3 .

Constraints:
1 <= S <= 10

Expected Complexities
Time Complexity: O(n^2)
Auxiliary Space: O(1)
*/

//Code

class Solution {
    public static void invTriangleWall(int s) {

        for(int i = s; i>0; i--) {
            for(int j = i; j>0; j--) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}