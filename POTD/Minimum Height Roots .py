# Minimum height roots

# You are given an undirected graph, which has tree characteristics with V vertices numbered from 0 to V-1 and E edges, 
# represented as a 2D array edges[][], where each element edges[i] = [u, v] represents an edge from vertex u to v.

# You can choose any vertex as the root of the tree. Your task is to find all the vertices that, when chosen as the root, 
# result in the minimum possible height of the tree.

# Note: The height of a rooted tree is defined as the maximum number of edges on the path from the root to any leaf node.

# Examples: 

# Input: V = 5, E = 4, edges[][] = [[0, 2], [1, 2], [2, 3], [3, 4]]
# Output: [2, 3]
# Explanation: If we choose vertices 2 or 3 as the root, the resulting tree has the minimum possible height, which is 2.

# Input: V = 4, E = 3, edges[][] = [[0, 1], [0, 2], [0, 3]]
# Output: [0]
# Explanation: Only vertex 0 as root gives the minimum possible height, which is 1.

# Constraints:
# 1 ≤ V ≤ 105
# 0 ≤ E ≤ V-1
# 0 ≤ edges[i][0], edges[i][1] < V

#Code

from collections import defaultdict, deque
class Solution:
    def minHeightRoot(self, V, edges):
        if V == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * V

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        leaves = deque()
        for i in range(V):
            if degree[i] == 1:
                leaves.append(i)

        remaining_nodes = V
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)