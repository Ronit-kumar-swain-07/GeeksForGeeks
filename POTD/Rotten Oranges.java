/*
Rotten Oranges

Given a matrix mat[][], where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges

Your task is to determine the minimum time required so that all the oranges become rotten. A rotten orange at index (i, j),
can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

Note: If it is impossible to rot every orange then simply return -1.

Examples:

Input: mat[][] = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
Output: 2
Explanation: 
Oranges at positions (0,0), (0,3), (1,3), and (2,3) will rot adjacent fresh oranges in successive time frames.
All fresh oranges become rotten after 2 units of time.

Input: mat[][] = [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
Output: -1
Explanation: Oranges at positions (0,0), (0,3), (1,3), and (2,3) rot some fresh oranges,
but the fresh orange at (2,0) can never be reached, so not all oranges can rot.

Constraints:
1 ≤ mat.size() ≤ 500
1 ≤ mat[0].size() ≤ 500
mat[i][j] = {0, 1, 2} 
*/

class Solution {
    public boolean chkmat(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        for(int i = 0; i<m; i++) {
            for(int j = 0; j < n; j++) {
                if(mat[i][j] != 2) {
                    return false;
                }
            }
        }
        return true;
    }
    public int orangesRot(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int count = 0;
        while(!chkmat(mat)) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if(mat[i][j] == 2) {
                        if(mat[i-1][j] != 0 ) mat[i-1][j] ++;
                        else if(mat[i+1][j] != 0) mat[i+1][j] ++;
                        else if(mat[i][j-1] != 0) mat[i][j-1] ++;
                        else if(mat[i][j+1] != 0) mat[i][j+1] ++;
                        count++;
                        }
                    }
                }
            }
            return count;
        }
    }


// PYTHON
/*
class Solution:
    def orangesRot(self, mat):
        m, n = len(mat), len(mat[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 2:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        time = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while q:
            size = len(q)
            rotted = False

            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == 1:
                        mat[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
                        rotted = True

            if rotted:
                time += 1

        return time if fresh == 0 else -1
*/