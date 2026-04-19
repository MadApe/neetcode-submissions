class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_full_word = False

        root = TrieNode()

        for word in strs:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_full_word = True
    
        prefix = []
        node = root
        while True:
            if len(node.children) != 1:
                break

            if node.is_full_word:
                break

            c = next(iter(node.children))
            prefix.append(c)
            node = node.children[c]

        return "".join(prefix)
