def isvalid(arr, i, j, n):
    if i >= 0 and i < n and j >=0 and j < n:
        return True

def maze(arr, i, j, n, visited):
    if i == n - 1 and j == n - 1:
        global count
        count = count + 1
        return
    visited[i][j] = 1
    if isvalid(arr, i, j, n):
        if isvalid(arr, i - 1, j, n) and visited[i - 1][j]==0 and arr[i-1][j] == 0:
            maze(arr, i - 1, j, n, visited)

        if isvalid(arr, i + 1, j, n) and visited[i + 1][j] == 0 and arr[i+1][j] == 0:
            maze(arr, i + 1, j, n, visited)

        if isvalid(arr, i, j - 1, n) and visited[i][j - 1] == 0 and arr[i][j-1] == 0:
            maze(arr, i, j - 1, n, visited)

        if isvalid(arr, i, j + 1, n) and visited[i][j + 1] == 0 and arr[i][j+1] == 0:
            maze(arr, i, j + 1, n, visited)

        visited[i][j] = 0


visited = [[0] * 7 for i in range(7)]
arr = []
count = 0
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))
maze(arr, 0, 0, n, visited)
print(count)
