class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_cnt = 0


        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])

            grid[start_r][start_c] = "0"  # mark as visited immediately

            while queue:
                r, c = queue.popleft()

                directions = [(1,0), (-1,0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_cnt += 1
                    bfs(r,c)

        return island_cnt
