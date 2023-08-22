# morning algos
# neetcode Course Schedule

class Solution:
    def canFinish(self, numCourses, prerequisites):
        preReqMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preReqMap[course].append(pre)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preReqMap[course] == []:
                return True
            
            visit.add(course)

            for pre in preReqMap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            preReqMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True

    print(canFinish(2, [[1,0],[0,1]]))