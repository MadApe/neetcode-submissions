class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)
        result = []
        prefix_product = None
        suffix_product = None

        for i in range(len(nums)):
            reverse_i = len(nums) - 1 - i

            if prefix_product == None:
                prefix_product = nums[i]
            else:
                prefix_product *= nums[i]

            prefix[i] = prefix_product
            
            if suffix_product == None:
                suffix_product = nums[reverse_i]
            else:
                suffix_product *= nums[reverse_i]

            suffix[reverse_i] = suffix_product

        for i in range(len(nums)):
            reverse_i = len(nums) - 1 - i
            if i == 0:
                result.append(suffix[i + 1])
            elif i == len(nums) - 1:
                result.append(prefix[i - 1])
            else:
                result.append(prefix[i - 1] * suffix[i + 1])

        return result

            