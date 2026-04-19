class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        for n in nums:
            freq_dict[n] += 1

        freq_list = sorted([(count, num) for num, count in freq_dict.items()])

        return [num for count, num in freq_list[-k:]]


        


        