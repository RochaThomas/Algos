# morning algos
# neetcode Course Schedule II

class Solution:
    def findOrder(self, numCourses, prerequisites):
        visited = set()
        res = []

        preMap = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle = set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res

    print(findOrder(2, [[1,0]]))