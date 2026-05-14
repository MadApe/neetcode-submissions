class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # until the low and high pointers "overlap"
        while low <= high:
            mid = (low + high) // 2  # index of the midpoint of the sub-array
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                # left side is sorted
                if target >= nums[low] and target < nums[mid]:
                    # if the target is in the range of the sorted side (left),
                    # then look left, else look right
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # right side is sorted
                if target > nums[mid] and target <= nums[high]:
                    # if the target is in the range of the sorted side (right),
                    # then look right, else look left
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
