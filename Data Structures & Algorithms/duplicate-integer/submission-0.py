class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()

        for v in nums:
            if v in seen:
                return True
            else:
                seen[v] = True

        return False
        