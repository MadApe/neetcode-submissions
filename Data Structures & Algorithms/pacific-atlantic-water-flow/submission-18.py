class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Boundary Guard: Handle empty or malformed grids
        if not heights or not heights[0]:
            return []
            
        rows, cols = len(heights), len(heights[0])
        
        # Storage for all cells that can reach each respective ocean
        pacific_visited = set()
        atlantic_visited = set()
        
        def dfs(r, c, prev_height, visited_set):
            # 1. Base Case: Out of grid bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
                
            # 2. Base Case: Cyclic Guard (Already tracked this cell for this ocean)
            if (r, c) in visited_set:
                return
                
            # 3. Base Case: Flow Guard
            # If current cell is SHORTER than the previous cell, water cannot flow 
            # downhill from here to the ocean. Halt this path.
            if heights[r][c] < prev_height:
                return
                
            # Action: This cell successfully connects to the ocean! Record it.
            visited_set.add((r, c))
            
            # Recursive Step: Explore all 4 cardinal directions uphill
            dfs(r + 1, c, heights[r][c], visited_set) # Down
            dfs(r - 1, c, heights[r][c], visited_set) # Up
            dfs(r, c + 1, heights[r][c], visited_set) # Right
            dfs(r, c - 1, heights[r][c], visited_set) # Left

        # ----------------------------------------------------
        # TRIGGER SEEDS: Start at the coastlines and walk inland
        # ----------------------------------------------------
        
        # Step 1: Top and Bottom Rows (Horizontal Coastlines)
        for c in range(cols):
            # Top Row -> Abuts the Pacific Ocean
            dfs(0, c, heights[0][c], pacific_visited)
            
            # Bottom Row -> Abuts the Atlantic Ocean
            dfs(rows - 1, c, heights[rows - 1][c], atlantic_visited)
            
        # Step 2: Left and Right Columns (Vertical Coastlines)
        for r in range(rows):
            # Left Column -> Abuts the Pacific Ocean
            dfs(r, 0, heights[r][0], pacific_visited)
            
            # Right Column -> Abuts the Atlantic Ocean
            dfs(r, cols - 1, heights[r][cols - 1], atlantic_visited)
            
        # ----------------------------------------------------
        # COMBINE STEP: Find the intersection of both sets
        # ----------------------------------------------------
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r, c])
                    
        return result