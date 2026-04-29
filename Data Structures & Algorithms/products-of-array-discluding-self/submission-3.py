class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        product = None

        for i, n in enumerate(nums):
            product = None
            for j, n2 in enumerate(nums):
                if i != j:
                    if product == None:
                        product = n2
                    else:
                        product *= n2
            
            results.append(product)

        return results

            