class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ""
        max_len = cur_len = 0

        for c in s:
            if c in sub_str:
                index = sub_str.index(c)
                sub_str = sub_str[index + 1:]
                cur_len = len(sub_str)

            sub_str += c
            cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len