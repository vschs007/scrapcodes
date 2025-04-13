from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt=0
        i=0
        j=i+2
        while(i<len(nums)and j<len(nums)):
            if nums[i]+nums[j]==0 and nums[i+1]!=0:
                cnt+=0
            elif 2*(nums[i]+nums[j])==nums[i+1]:
                cnt+=1
            i+=1
            j+=1
        return cnt

s= Solution()
print(s.countSubarrays([1,2,1,4,1]))