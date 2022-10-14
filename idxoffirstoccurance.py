class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needle in haystact
        ws = len(needle)
        i = 0
        j = i + ws - 1
        while (j < len(haystack)):
            temp = haystack[i:j + 1]
            if temp == needle:
                return i
            j += 1
            i += 1
        return -1


