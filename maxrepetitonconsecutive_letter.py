strr = "aabaaabbccccczzxzzzziio"
temp = list(set(strr))
count = 0
maxcount =0
res=[]
for i in range(len(temp)):
    for j in range(len(strr)):
        if strr[j]==temp[i]:
            count+=1
        else:
            maxcount = max(maxcount,count)
            count = 0

    res.append([temp[i],maxcount])
    maxcount = 0
print(res)
