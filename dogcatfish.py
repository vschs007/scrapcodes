class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        slist = s.split(" ")
        patternlist = list(pattern)
        setlist=set(slist)
        setpattern = set(patternlist)
        seenvals =set()
        if len(setlist)!=len(setpattern) or len(patternlist)!=len(slist):
            return False
        for i in range(len(patternlist)):
            if patternlist[i] not in map:
                if slist[i] not in seenvals:
                    map[patternlist[i]]=slist[i]
                    seenvals.add(slist[i])
                else:
                    return False

            else:
                if map[patternlist[i]]!=slist[i]:
                    return False
        return True

s = Solution()
print(s.wordPattern("aaa","aa aa aa aa"))