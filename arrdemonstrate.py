from typing import List


def merge(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr)  # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n):

        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])

        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans


arr = [[1,3],[2,6],[7,10]]

print(merge(arr))
