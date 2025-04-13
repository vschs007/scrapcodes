from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """

        :rtype: object
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
        prevRows.append(newRow)
        return prevRows
    
s = Solution()
print(s.generate(4))