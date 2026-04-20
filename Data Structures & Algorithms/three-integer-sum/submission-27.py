class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            n = nums[i]

            while l < r:
                ln = nums[l]
                rn = nums[r]
                summed = n + ln + rn
                if summed == 0:
                    values = [n, ln, rn]
                    l += 1
                    r -= 1
                    triplets.append(values)
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif summed < 0:
                    l += 1
                else:
                    r -= 1


        return triplets
