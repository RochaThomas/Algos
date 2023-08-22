# morning algos
# neetcode Course Schedule II

class Solution:
    def findOrder(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        cycle = set()
        taken = set()
        res = []
        def dfs(course):
            if course in cycle:
                return False
            if course in taken:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            cycle.remove(course)
            taken.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []

        return res

    print(findOrder(2, [[1,0]]))