class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)
        if len2 > len1:
            return ""
        haspat = {}
        hasstr = {}
        for i in range(len2):
            if haspat.get(t[i]) is None:
                haspat[t[i]] = 0
            haspat[t[i]] += 1

        count = 0
        left = 0
        startindex = -1
        minlen = 9999999999

        for right in range(len1):
            if hasstr.get(s[right]) is None:
                hasstr[s[right]] = 0
            hasstr[s[right]] += 1

            if haspat.get(s[right]) is None:
                haspat[s[right]] = 0
            if hasstr.get(s[right]) <= haspat.get(s[right]):
                count += 1
            if count == len2:
                while (hasstr.get(s[left]) > haspat.get(s[left])):
                    hasstr[s[left]] -= 1
                    left += 1
                windowlen = right - left + 1
                if minlen > windowlen:
                    minlen = windowlen
                    startindex = left
        if startindex == -1:
            return ""
        else:
            return s[startindex:startindex + minlen]


ss= Solution()

s = "ADOBECODEBANC"
t = "ABC"
print(ss.minWindow(s,t))