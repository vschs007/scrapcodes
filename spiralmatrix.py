from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)  # take top row
            if matrix and matrix[0]:
                # rotate remaining matrix counter-clockwise
                matrix = list(zip(*matrix))[::-1]
        return res


s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
