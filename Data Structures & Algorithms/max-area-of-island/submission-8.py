class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r, c) -> int:
            # validate boundries and whether we are looking at land
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0

            grid[r][c] = 0  # mark this cell as visited

            # pieces of land is this cell (1) + the result of a dfs in each direction
            pieces = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return pieces

        # iterate over the matric, finding the area of each island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area



            