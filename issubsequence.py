class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            look = s[i]
            if t[j] != look:
                j += 1
                continue
            i += 1
            j += 1

        if j == len(t) and i < len(s):
            return False
        else:
            return True


s = Solution()
print(s.isSubsequence("axc","ahbgdc"))