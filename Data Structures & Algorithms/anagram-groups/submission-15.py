class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_lists = dict()
        grouped_strs = list()
        for i in range(len(strs)):
            str1 = strs[i]
            sorted_str = ''.join(sorted(str1))
            if sorted_str not in sorted_lists:
                sorted_lists[sorted_str] = []

            sorted_lists[sorted_str].append(str1)

        for k, v in sorted_lists.items():
            grouped_strs.append(v)

        return grouped_strs
