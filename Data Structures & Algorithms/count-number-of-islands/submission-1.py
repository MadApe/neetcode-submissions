class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_cnt = 0

        def dfs(r, c):
            # base case/boundry - if r or c is out of range or the cell is water, return
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == '0'):
                return

            # mark this cell as visited (water) since we don't need to count this twice
            grid[r][c] = '0'

            dfs(r + 1, c)  # search down
            dfs(r - 1, c)  # search up
            dfs(r, c + 1)  # search right
            dfs(r, c - 1)  # search left

        # iterate over the matrix and call dfs when we find land, counting the islands as we go
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # found an island
                    island_cnt += 1
                    dfs(r, c)  # flood the entire island so we don't visit it again

        return island_cnt

