# morning algos
# neetcode Course Schedule II

class Solution:
    def findOrder(self, numCourses, prerequisites):
        res = []
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)    
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res


    print(findOrder(2, [[1,0]]))