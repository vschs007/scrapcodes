from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]==i:
                continue
            else:
                return i
        return i+1