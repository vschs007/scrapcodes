def findmex(arr):
    c = set()
    for i in range(max(arr) + 1):
        c.add(i)
    for i in range(len(arr)):
        try:
            c.remove(arr[i])
        except:
            continue

    if(len(c)>0):
        return list(c)[0]
    else:
        return max(arr)+1
arr = [0,1,2,3,4]
res = -1
# generate subarray from the given subarray
for i in range(1, len(arr) - 1):
    k = findmex(arr[:i])
    l = findmex(arr[i:])
    if k == l:
        res = i
        break

if res > 0:
    print(res)
else:
    print(-1)
