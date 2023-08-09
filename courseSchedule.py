# morning algos
# neetcode Course Schedule

class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for x, y in prerequisites:
                preMap[y].append(x)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

    print(canFinish(2, [[1,0],[0,1]]))