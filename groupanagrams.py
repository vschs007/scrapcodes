from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        ans = []
        for s in strs:
            hashed = "".join(sorted(s))
            if hashed not in m:
                m[hashed] = []
                m[hashed].append(s)
            else:
                m[hashed].append(s)
        for i in m.values():
            ans.append(i)
        return ans


s= Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))