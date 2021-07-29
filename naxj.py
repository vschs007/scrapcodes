s = "aaaaaccdvgggtttj"
k = 2
lsf = 1
currlen = 1
res = []
dist = 1
l = 0
r = 0
for i in range(0, len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            currlen += 1
        elif s[i] != s[j] and dist <= k:
            dist += 1
            if dist > k:
                lsf = max(currlen, lsf)
                l = i
                r = j
                break
            else:
                currlen += 1
        i = i + 1

print(l, r)
