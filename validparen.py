class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        else:
            valid_range = ["[]", "{}", "()"]
            for i in range(1, len(s), 2):
                if s[i - 1:i+1] not in valid_range:
                    return False

            return True

sol = Solution()

print(sol.isValid("()[]{}"))
