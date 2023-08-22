# morning algos
# neetcode Course Schedule

class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            for pre in preMap[course]:
                if not dfs(pre): return False

            visited.remove(course)
            preMap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False

        return True


        

    print(canFinish(2, [[1,0],[0,1]]))