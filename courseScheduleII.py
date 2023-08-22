# morning algos
# neetcode Course Schedule II

class Solution:
    def findOrder(self, numCourses, prerequisites):
        prereqMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqMap[course].append(pre)
        visit = set()
        taken = set()
        res = []
        def dfs(course):
            if course in visit:
                return False
            if course in taken:
                return True
            visit.add(course)
            for pre in prereqMap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            taken.add(course)
            res.append(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course): return []
        return res

    print(findOrder(2, [[1,0]]))