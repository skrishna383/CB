class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            preMap[i].append(j)
        visitset=set()
        def dfs(n):
            if n in visitset:
                return False
            if preMap[n]==[]:
                return True
            visitset.add(n)
            for prereq in preMap[n]:
                if not dfs(prereq): return False   
            visitset.remove(n) 
            preMap[n]=[]
            return True

        for i in range(numCourses):
            if not  dfs(i): return False
        return True