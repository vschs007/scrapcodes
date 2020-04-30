def IsSparse(mat):
    count = 0
    rows = len(mat)
    cols = len(mat[0])
    size = rows * cols
    for i in range(0, rows):
        for j in range(0, cols):
            if (mat[i][j] == 0):
                count = count + 1
    if (count > (size / 2)):
        return True
    else:
        return False

a = [
    [4.0, 0.1, 0.6],
    [0, 5, 0],
    [0, 0, 6]
]
print(IsSparse(a))
