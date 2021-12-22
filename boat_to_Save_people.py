from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the array 1 2 2 3   ,3
        people = sorted(people)
        low = 0
        ans = 0
        high = len(people) - 1
        while (low <= high):
            if low == high:
                ans += 1
                break
            if people[low] + people[high] <= limit:
                ans += 1
                low += 1
                high -= 1
            if people[low] + people[high] > limit:
                ans += 1
                high -= 1
        return ans

a= Solution()
print(a.numRescueBoats([1,2,2,1],3))