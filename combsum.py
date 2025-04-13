from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(combinations, remaining,index):
            if remaining ==0:
                result.append(list(combinations))
                return
            if remaining < 0:
                return
            for i in range(index,len(candidates)):
                val = candidates[i]
                if remaining-val <0:
                    break
                combinations.append(val)
                backtrack(combinations,remaining-val,i)
                combinations.pop()

        backtrack([],target,0)
        return result

s = Solution()
print(s.combinationSum([2,3,6,7],7))
