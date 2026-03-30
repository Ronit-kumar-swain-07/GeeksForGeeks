class Solution:
    def articulationPoints(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        disc = [-1] * V
        low = [-1] * V  
        visited = [False] * V
        isAP = [False] * V  
        self.timer = 0
        def dfs(u, parent):
            visited[u] = True
            disc[u] = low[u] = self.timer
            self.timer += 1
            
            children = 0
            
            for v in adj[u]:
                
                if v == parent:
                    continue
                
                if not visited[v]:
                    children += 1
                    dfs(v, u)
                    low[u] =min(low[u],low[v])
                    if parent != -1 and low[v] >= disc[u]:
                        isAP[u] = True
                else:
                    low[u] = min(low[u], disc[v])
            
            if parent == -1 and children > 1:
                isAP[u] = True
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)
        result = [i for i in range(V) if isAP[i]]
        
        return result if result else [-1]