class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return image
        
        rows = len(image)
        cols = len(image[0])

        # if the given cell is out of range or is already the color, return the original image
        if (sr < 0 or sr >= rows or
            sc < 0 or sc >= cols):
            return image

        original_color = image[sr][sc]
        if original_color == color:
            return image

        def dfs(r, c):
            # validate its a valid cell and the 
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                image[r][c] != original_color):
                return

            # change the color and visit neighboring cells
            image[r][c] = color
            dfs(r + 1, c)  # up
            dfs(r - 1, c)  # down
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

            return

        dfs(sr, sc)

        return image