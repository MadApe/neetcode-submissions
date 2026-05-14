class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2

        while low < high:
            if nums[mid] > nums[high]:
                low = mid + 1  # min can't be minimum because we just learned nums[high] is smaller
            else:
                high = mid

            mid = (low + high) // 2

        return nums[high]
                

