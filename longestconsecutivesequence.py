from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums =list(set(nums))
        nums.sort()
        idx = []
        ans = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                idx.append(i)
        start = 0

        for i in range(len(idx)):
            ans.append(nums[start:idx[i]])
            start = idx
        ans.append(nums[start[0]:])


        return len(max(ans, key=lambda x: len(x))) if len(idx)!=0 else len(nums)
s = Solution()
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))

