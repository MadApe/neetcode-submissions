class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in num_set:
            curr_len = 1
            next_n = n + 1
            while next_n in num_set:
                curr_len += 1
                next_n += 1
            
            max_len = max(max_len, curr_len)

        return max_len

