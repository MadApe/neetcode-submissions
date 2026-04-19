class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        root_word = strs[0]

        for i in range(len(root_word)):
            c = root_word[i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != c:
                    return "".join(prefix)

            prefix.append(c)

        return "".join(prefix)
