from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                newarr = nums[0:i] + nums[j:]
                if newarr == sorted(newarr):
                    count += 1
        return count


s = Solution()
nums = [6,5,7,8]
print(s.incremovableSubarrayCount(nums))