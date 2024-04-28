class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        t = list(t)
        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i]
        return t[i+1]


s = Solution()

print(s.findTheDifference("ae","aea"))