class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        # print(f"rows={rows}, cols={cols}")

        def dfs(r, c) -> int:
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0

            grid[r][c] = 0

            # right = dfs(r + 1, c)
            # left  = dfs(r - 1, c)
            # up    = dfs(r, c + 1)
            # down  = dfs(r, c - 1)

            # print(f"right={right}, left={left}, up={up}, down={down}")

            pieces = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return pieces

        for r in range(rows):
            for c in range(cols):
                # print(f"processing ({r}, {c})")
                if grid[r][c] == 1:
                    
                    area = dfs(r, c)
                    # print(area)
                    max_area = max(max_area, area)

        return max_area



            