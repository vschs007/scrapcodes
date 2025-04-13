from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # 50 12 5 3 2 1 
        arr = [0] * len(nums)
        nums = sorted(nums)
        arr[0] = nums[0]
        for i in range(1, len(nums)):
            arr[i] = arr[i - 1] + nums[i]

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < arr[i - 1]:
                return arr[i]
        return -1

s= Solution()
nums = [1,12,1,2,5,50,3]
print(s.largestPerimeter(nums))