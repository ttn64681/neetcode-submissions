class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=len(prerequisites)
        if n==0: return True

        prereq_map=defaultdict(list)
        for a,b in prerequisites:
            prereq_map[a].append(b)

        processed=set()
        path=set()
        # print(prereq_map)
        def traverse_prereqs(i) -> bool:
            # print(f"i is {i}")
            if i in path: 
                # print("found in path. we out FALSE\n")
                return False # circular
            if i in processed:
                # print("found in processed. we out True\n")
                return True # circular
            path.add(i)
            if i in prereq_map: # prereq has another prereq
                for x in prereq_map[i]:
                    # print(f"{x} has another prereq....")
                    if not traverse_prereqs(x): return False
            
            path.remove(i)
            processed.add(i)
            # print(f"finished processing {i}")
            return True

        for a,_ in prerequisites:
            if a in processed: continue
            if not traverse_prereqs(a):
                return False
        return True


