# Length of Longest Cycle in a Graph
# Given an directed graph with V vertices numbered from 0 to V-1 and E edges, represented as a 2D array edges[][], 
# where each entry edges[i] = [u, v] denotes an edge between vertices u and v. Each node has at most one outgoing edge.

# Your task is to find the length of the longest cycle present in the graph. If no cycle exists, return -1.

# Note: A cycle is a path that starts and ends at the same vertex.

# Examples :

# Input: V = 7, edges[][] = [[0, 5], [1, 0], [2, 4], [3, 1], [4, 6], [5, 6], [6, 3]]
# Output: 5
# Explanation: longest Cycle is 0->5->6->3->1->0

# Input: V = 8, edges[][] = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 1], [5, 4], [6, 2], [7, 6]]
# Output: 4
# Explanation: longest Cycle is 0->1->2->3->0

# Constraints:
# 1 ≤ V, E ≤ 104
# 0 ≤ edges[i][0], edges[i][1] < V

#Code
class Solution:
    def longestCycle(self, V, edges):
        outgoing = [-1] * V
        for u, v in edges:
            outgoing[u] = v
        visited = [False] * V
        max_cycle = -1
        for i in range(V):
            if visited[i]:
                continue
            node = i
            step = 0
            path = {}
            while node != -1 and not visited[node]:
                visited[node] = True
                path[node] = step
                node = outgoing[node]
                step += 1
                if node in path:
                    max_cycle = max(max_cycle, step - path[node])
                    break

        return max_cycle