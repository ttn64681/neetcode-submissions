"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node

        #hashmap={val:clone_Node}
        #for each nbr, create copy of nbr
        hmap=defaultdict(Node)
        q=collections.deque() # anything in q has cpy

        new = Node(node.val) # copy of given node
        hmap[node]=new
        q.append(node)
        #[1: 2,3] [2: 1] [3: 1,4] [4: 1]
        #{}
        #[]

        while q:
            cur=q.pop() # starts as new
            for n in cur.neighbors:
                if n not in hmap: # if nbr has no cpy
                    q.append(n)
                    cpy=Node(n.val) # create cpy
                    hmap[n]=cpy # add nbr cpy to map
                copy=hmap[n]
                hmap[cur].neighbors.append(copy) # add nbr copy to nbrs of cur
                

        return new
                    
                    
                
        
        


        