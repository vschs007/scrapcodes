from itertools import permutations


def Remove(lst):
    return ([list(i) for i in {*[tuple(sorted(i)) for i in lst]}])
strs = ["eat","tea","tan","ate","nat","bat"]
n = len(strs)
resarr=[]
i=0
while(i<n):
    tmparr=[]
    word = strs[i]
    tmparr.append(word)
    for j in range(n):
        if j ==i:
            continue
        else:
            if sorted(word)==sorted(strs[j]):
                tmparr.append(strs[j])
    resarr.append(tmparr)
    i+=1

k = [sorted(k) for k in resarr]
print(Remove(k))


