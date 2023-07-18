from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n[0]
        elif n == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        low = 0
        high = n - 1
        while (low <= high):
            mid = (low + high) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[low]<=nums[mid] and nums[mid]>nums[high]:
                low=mid+1
            else:
                high = mid-1
        return nums[low]

s= Solution()
a=[11,13,15,17]
print(s.findMin(a))


