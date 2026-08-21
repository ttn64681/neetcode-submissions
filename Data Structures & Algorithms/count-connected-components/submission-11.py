class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # originally n disjoint sets/forests
        res=n
        # track if part of forest/set: common root parent
        parent=[i for i in range(n)] # n=5: [0,1,2,3,4]
        def root(n):
            # if n's parent is n itself, that is root
            while n!=parent[n]: # modify the parent arr to be the root (why not)
                parent[n] = parent[parent[parent[n]]] # check great-grand-parent
                n = parent[n] 
            return n

        # for each edge, merge w/ root parent
        ## n=7, [[0,1],[0,2],[2,3],[5,6],[1,2],[4,5]]
        rank=[1]*n
        def union(n1,n2):
            r1, r2 = root(n1), root(n2)
            if r1 == r2:
                return 0
            if rank[r1]>=rank[r2]:
                parent[r2] = r1
                rank[r1] += rank[r2]
            else:
                parent[r1] = r2
                rank[r2] += rank[r1]
            return 1

        # if no common root parent -> that means merged new node to forest/set
        ## if merging new node -> decrement amount of disjoint sets
        for n1,n2 in edges:
            res -= union(n1,n2)
            # print(f"i:[{n1},{n2}] res:{res}\n")
        return res
