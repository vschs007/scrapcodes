from itertools import  permutations
import itertools
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        alllist = list(itertools.permutations(words))
        newlist=[]
        ans=[]
        for k in alllist:
            newlist.append("".join(k))
        for k in newlist:
            if k in s:
                indices = [i for i in range(len(s)) if s.startswith(k, i)]
                ans.extend(indices)

        return sorted(set(ans))

sl = "fffffffffffffffffffffffffffffffff"
words = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]

s = Solution()
print(s.findSubstring(sl,words))