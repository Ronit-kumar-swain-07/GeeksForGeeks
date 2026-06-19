class Solution {
    public boolean isToeplitz(int[][] mat) {
        // code here
        int m = mat.length;
        int n = mat[0].length;
        for(int i = 0; i < m-1; i++) {
            for(int j = 0; j < n-1; j++) {
                if(mat[i][j] != mat[i+1][j+1]) {
                return false;
                }
            }
        }
        return true;
    }
}