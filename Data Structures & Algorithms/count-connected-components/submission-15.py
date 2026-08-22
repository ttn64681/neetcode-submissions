class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        seen=[0 for _ in range(n)]
        adj=[[] for _ in range(n)]
        for u,v in edges: # O(V+E)
            adj[u].append(v)
            adj[v].append(u)

        def dfs(n):
            for nbr in adj[n]:
                if seen[nbr]==0:
                    seen[nbr]=1
                    dfs(nbr)
        
        for i in range(n):
            if seen[i]==0:
                dfs(i)
                count+=1
        return count

