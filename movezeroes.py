from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        counzero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counzero += 1
        s = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[s] = nums[i]
                s += 1
        for i in range(len(nums) - 1, len(nums) - counzero - 1, -1):
            nums[i] = 0

        return nums