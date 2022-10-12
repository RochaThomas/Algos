# morning algos
# neetcode Course Schedule

class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True

    print(canFinish(2, [[1,0],[0,1]]))