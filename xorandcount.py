def xorsum(arr):
    arr = list(arr)
    res = arr[0]
    n = len(arr)
    for i in range(1, n):
        res^= arr[i]
    if res + 1 == res^1:
        return True
    else:
        return False


def solve(N, M, A, queries):
    resarr = []
    # Write your code here
    # range index 1 follow krta hai,
    # [1,5] to sab subset banao aur calculate kro
    for i in range(M):
        count = 0
        l, r = queries[i][0], queries[i][1]
        for j in range(l - 1, r - 1):
            for k in range(j, r):
                tmparr = A[j:k+1]

                if xorsum(tmparr):
                    count += 1
                else:
                    continue
        resarr.append(count)
    return resarr



N = int(input())
M = int(input())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for i in range(M)]

out_ = solve(N, M, A, queries)
print(' '.join(map(str, out_)))