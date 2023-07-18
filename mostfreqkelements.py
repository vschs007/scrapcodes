s= [0,3,7,2,5,8,4,6,0,1]
t=2
mp ={}
for k in s:
    if k in mp:
        mp[k]+=1
    else:
        mp[k]=1

lst = list(mp.items())
lst.sort(key=lambda x:x[1],reverse=True)
print(lst)
res=[]
for i in range(t):
    res.append(lst[i][0])

print(res)