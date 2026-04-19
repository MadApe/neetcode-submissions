class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        mid = (r - l) // 2

        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return True
        #     else:
        #         return False

        while l <= r:
            mid_val = nums[mid]
            print(f"l={l}, r={r}, mid={mid}, mid_val={nums[mid]}, target={target}")
            if mid_val == target:
                return True

            # identify which side of the list is sorted
            if nums[l] < nums[mid]:
                # left side is sorted
                print(f"left side is sorted")
                if target >= nums[l] and target < nums[mid]:
                    print(f"target must be on left")
                    r = mid - 1
                else:
                    print(f"target must be on right")
                    l = mid + 1
            elif nums[l] > nums[mid]:
                print(f"right side is sorted")

                # right side is sorted
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                    print(f"target must be on right")
                else:
                    print(f"target must be on left")
                    r = mid - 1
            else:
                print(f"cannot tell which side is sorted")
                # must be duplicates so increment l until we know which side is sorted
                l += 1               
            
            mid = ((r - l) // 2) + l
        
        return False

