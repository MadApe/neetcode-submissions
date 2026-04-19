class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = ((r - l) // 2) + l

            if nums[mid] == target:
                return True

            # identify which side of the list is sorted
            if nums[l] < nums[mid]:
                # left side is sorted
                if nums[l] <= target < nums[mid]:
                    # the target must be on the sorted side -> look left
                    r = mid - 1
                else:
                    # the target is not on the sorted side -> look right
                    l = mid + 1
            elif nums[l] > nums[mid]:
                # right side is sorted
                if nums[mid] < target <= nums[r]:
                    # the target is on the sorted side -> look right
                    l = mid + 1
                else:
                    # the target is not on the sorted side -> look left
                    r = mid - 1
            else:
                # must be duplicates so increment l until we know which side is sorted
                l += 1               
            
            
        
        return False

