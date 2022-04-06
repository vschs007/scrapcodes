from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = sum(nums)
        if res % 2 != 0:
            return False
        else:
            res = res // 2
            dp = [[None for i in range(res + 1)] for j in range(len(nums) + 1)]
            for i in range(len(nums) + 1):
                for j in range(res + 1):
                    if i == 0 and j == 0:
                        dp[i][j] = True
                    elif i == 0:
                        dp[i][j] = False
                    elif j == 0:
                        dp[i][j] = True
                    else:
                        if dp[i - 1][j] == True:
                            dp[i][j] = True
                        else:
                            val = nums[i - 1]
                            if j >= val:
                                if dp[i - 1][j - val] == True:
                                    dp[i][j] = True
                                else:
                                    dp[i][j] = False
            return dp[len(nums)][res]
