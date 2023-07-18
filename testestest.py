def computeDeviceCrossovers(n, websiteVisits, m, appVisits):
    res = []
    cnt = 0
    if n == 0 or m == 0:
        return 0
    for i in range(n):
        res.append([websiteVisits[i], 'w'])
    for i in range(m):
        res.append([appVisits[i], 'a'])
    res = sorted(res)

    for i in range(1, len(res)):
        if res[i - 1][1] != res[i][1]:
            cnt += 1
    return cnt


n = int(input())
websiteVisits = []
appVisits = []
for i in range(n):
    temp = int(input())
    websiteVisits.append(temp)
m = int(input())
for i in range(m):
    temp = int(input())
    appVisits.append(temp)

out_ = computeDeviceCrossovers(n, websiteVisits, m, appVisits)
print(out_)