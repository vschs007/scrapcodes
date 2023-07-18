from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low =0
        high =n-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                if mid-1==-1:
                    return 0
                elif nums[mid-1]<=target:
                    return mid-1
                else:
                    high = mid-1
            else:
                if mid+1==n:
                    return n
                elif nums[mid+1]>=target:
                    return mid+1
                else:
                    low=mid+1
ss =Solution()
ar =[1,3,5,6]
t=2
print(ss.searchInsert(ar,t))