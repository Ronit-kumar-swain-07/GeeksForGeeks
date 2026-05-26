import java.util.ArrayList;
class Solution {
    static ArrayList<Integer> diagView(int mat[][]) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        int n = mat.length;
        int idx;
        for(int j = 0; j < n; j++){
            int i = 0;
            while(i < j+1) {  
                idx = j;
                res.add(mat[i][idx]);
                i++;
            }
        }
        return res;
    }
}