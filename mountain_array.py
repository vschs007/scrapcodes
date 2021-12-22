from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        maxele = max(arr)
        ind = arr.index(maxele)
        if ind == 0 or ind == len(arr) - 1:
            return False
        for i in range(1, ind + 1):
            if arr[i] <= arr[i - 1]:
                return False
            else:
                continue
        for j in range(ind + 1, len(arr)):
            if arr[j - 1] <= arr[j]:
                return False

        return True
#  2 loop solution it was

#single loop sol
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr) < 3):
            return False
        i = 1
        while (i < len(arr) and arr[i] > arr[i - 1]):
            i += 1

        if i == 1 or i == len(arr):
            return False
        while (i < len(arr) and arr[i] < arr[i - 1]):
            i += 1

        return i == len(arr)

