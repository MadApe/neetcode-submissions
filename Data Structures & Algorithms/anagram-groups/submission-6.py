class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(a: str, b: str) -> boolean:
            seen_c = dict()

            for c in a:
                if c in seen_c:
                    seen_c[c] += 1
                else:
                    seen_c[c] = 1

            for c in b:
                if c not in seen_c:
                    return False
                else:
                    seen_c[c] -= 1

            for k, v in seen_c.items():
                if v != 0:
                    return False
            
            return True

        groups = list()
        seen_str = dict()  # tracks if the word is already in a group

        for i in range(len(strs)):
            s1 = strs[i]
            group = list()
            if s1 in seen_str:
                continue

            s1_len = len(s1)
            group.append(s1)
            seen_str[s1] = True

            for j in range(i + 1, len(strs)):
                s2 = strs[j]
                if len(s2) != s1_len:  # length doesn't match...cannot be an anagram
                    next
                
                if s2 in seen_str:  # we've already seen this string and grouped it
                    next

                # could still be an anagram, so let's check
                if isAnagram(s1, s2):
                    group.append(s2)
                    seen_str[s2] = True
            
            groups.append(group)
        
        return groups


        
                
            

            

