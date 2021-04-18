# cook your dish here
def find_index(arr, n, K):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == K:
            return mid
        elif arr[mid] < K:
            start = mid + 1
        else:
            end = mid-1
    return end + 1


t = int(input())
for test in range(t):
    n, m = map(int, input().split())
    resT = []
    l = []
    p = []
    for i in range(n):
        left, r = map(int, input().split())
        resT.append([left, r])
        l.append(left)
    for j in range(m):
        p.append(int(input()))

    print(resT)
    print(l)
    print(p)

    resT.sort()
    print(resT)
    l.sort()
    for i in range(m):
        time = p[i]
        ind = find_index(l, n, time)
        if(ind == 0):
            if(l[ind] == time):
                print(0)
            else:
                print(l[0]-time)
        elif(ind == n):
            if(resT[ind-1][1] > time):
                print(0)
            else:
                print(-1)
        else:
            if(resT[ind-1][1] > time):
                print(0)
            else:
                print(l[ind]-time)
