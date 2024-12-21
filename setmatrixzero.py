from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for l in range(len(matrix[0])):
                        if matrix[i][l]!=0:
                            matrix[i][l]='a'

                    for k in range(len(matrix)):
                        if matrix[k][j]!=0:
                            matrix[k][j] = 'a'


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='a':
                    matrix[i][j]=0

        return matrix



s = Solution()
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
