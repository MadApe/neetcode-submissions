class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}

        for i, n in enumerate(numbers):
            complement = target - n

            if complement in hash:
                return [hash[complement], i + 1]

            hash[n] = i + 1

        return []