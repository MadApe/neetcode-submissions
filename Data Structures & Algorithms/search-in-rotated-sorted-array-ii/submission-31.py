class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return True

            # identify which side of the list is sorted
            if nums[l] < nums[mid]: # left side is sorted
                if nums[l] <= target < nums[mid]:  # target on sorted side
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]: # right side is sorted
                if nums[mid] < target <= nums[r]:  # target on sorted side
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # can't determine sorted side due to duplicate values; incr until we can
                l += 1                       
        
        return False

