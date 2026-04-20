class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            # 1. Skip the same 'i' to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1

            while l < r:
                summed = nums[i] + nums[l] + nums[r]
                
                if summed == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 2. Skip the same 'l' to avoid duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # (Optional) Skip the same 'r'
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif summed < 0:
                    l += 1
                else:
                    r -= 1

        return triplets