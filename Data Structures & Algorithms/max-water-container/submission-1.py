class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            hl = heights[l]
            hr = heights[r]
            area = (r - l) * min(hl, hr)
            max_area = max(area, max_area)
            if hl < hr:
                l += 1
            else:
                r -= 1

        return max_area
        