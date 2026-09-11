class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        l=len(edges)
        if l==0: return True
        if l==1: return True
        seen=set()
        nbrs=defaultdict(list)

        for a,b in edges:
            nbrs[a].append(b)
            nbrs[b].append(a)
        print(nbrs)

        def dfs(a,parent):
            # print(f"on {a}")
            if a in seen:
                # print(f"seen {a}") 
                return False
            seen.add(a)
            if a in nbrs:
                for nb in nbrs[a]:
                    # print(f"checking nbr {nb}")
                    if nb==parent: continue
                    elif not dfs(nb,a): return False
            return True
        
        return dfs(edges[0][0],-1) and len(seen)==n
        # print(f"count={count} while n={n}")



            
