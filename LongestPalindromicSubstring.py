class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(ss):
            b = False
            ssrev = ss[::-1]
            if (ss == ssrev):
                b = True
            return b

        palindrome = ""
        for step in range(len(s)):
            for curr in range(len(s)):
                start = curr
                stop = curr + step + 1
                if stop > len(s):
                    break
                substr = s[start:stop]
                if isPalindrome(substr) and len(substr) > len(palindrome):
                    palindrome = substr
        return palindrome
