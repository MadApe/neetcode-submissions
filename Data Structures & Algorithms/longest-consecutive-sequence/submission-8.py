class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map_hash = {}
        sequence_starts = []

        for n in nums:
            map_hash[n] = 1

        for k in map_hash.keys():
            if (k - 1) not in map_hash:
                sequence_starts.append(k)

        max_len = 0

        for ss in sequence_starts:
            s_len = 1
            next_n = ss + 1
            while next_n in map_hash:
                s_len += 1
                next_n += 1
            
            max_len = max(s_len, max_len)

        return max_len
        

