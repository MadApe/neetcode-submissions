class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights) - 1):
            for j in range(i, len(heights)):
                h1 = heights[i]
                h2 = heights[j]
                area = min(h1, h2) * (j - i)
                max_area = max(max_area, area)

        return max_area
        