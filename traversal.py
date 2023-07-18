
def isPath(matrix, n):
    visited = [[False for x in range(n)]
               for y in range(n)]

    # Flag to indicate whether the
    # path exists or not
    flag = False

    for i in range(n):
        for j in range(n):
            if (matrix[i][j] == 1 and not
            visited[i][j]):
                if (checkPath(matrix, i,
                              j, visited)):
                    flag = True
                    break
    if (flag):
        print("YES")
    else:
        print("NO")

def isSafe(i, j, matrix):
    if (i >= 0 and i < len(matrix) and
            j >= 0 and j < len(matrix[0])):
        return True
    return False


def checkPath(matrix, i, j,
              visited):
    if (isSafe(i, j, matrix) and
            matrix[i][j] != 0 and not
            visited[i][j]):
        visited[i][j] = True

        if (matrix[i][j] == 2):
            return True

        # traverse up
        up = checkPath(matrix, i - 1,
                       j, visited)
        if (up):
            return True

        # Traverse left
        left = checkPath(matrix, i,
                         j - 1, visited)
        if (left):
            return True

        # Traverse down
        down = checkPath(matrix, i + 1,
                         j, visited)
        if (down):
            return True
        right = checkPath(matrix, i,
                          j + 1, visited)
        if (right):
            return True
    return False

if __name__ == "__main__":
    matrix = [[0, 3, 0, 1],
              [3, 0, 3, 3],
              [2, 3, 3, 3],
              [0, 3, 3, 3]]

    isPath(matrix, 4)

