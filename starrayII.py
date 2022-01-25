from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while (low < high):
            mid = (low + high) // 2
            if nums[mid] == nums[low]:
                low+=1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

s= Solution()
arr= [2,2,2,0,1]
print(s.findMin(arr))