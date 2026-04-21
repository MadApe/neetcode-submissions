class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}
        order = []
        visit_set = set()
        cycle_set = set()

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        
        def dfs(course: int) -> bool:
            if course in cycle_set:
                return False

            if course in visit_set:
                return True
            
            cycle_set.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            cycle_set.remove(course)
            visit_set.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return order
                
