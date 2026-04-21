class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find_root(n1):
            p = n1

            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find_root(n1), find_root(n2)

            if p1 == p2:
                return 0

            if rank[p2] >  rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1

        comp_count = n

        for n1, n2 in edges:
            comp_count -= union(n1, n2)
    
        return comp_count


