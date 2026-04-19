class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()

        for n in nums:
            if n in freq_dict:
                freq_dict[n] += 1
            else:
                freq_dict[n] = 1

        freq_list = sorted([(v, k) for k, v in freq_dict.items()], key=lambda t: t[0])

        top_k = []

        for t in freq_list[len(freq_list) - k:len(freq_list)]:
            top_k.append(t[1])

        return top_k


        


        