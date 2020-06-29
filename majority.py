import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        maxk = 0
        th = math.ceil(len(nums) / 2)
        nums1 = sorted(nums)
        if (len(nums1) == 1):
            return nums1[0]
        for i in range(1, len(nums1)):
            if (nums1[i - 1] == nums1[i]):
                count = count + 1
            if (count >= th):
                maxk = nums1[i]
                break
        return maxk

