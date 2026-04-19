class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i in range(len(nums)):
            n = nums[i]

            pair = target - n

            if pair in seen:
                return [seen[pair], i]

            if n not in seen:
                seen[n] = i

        return list()
        