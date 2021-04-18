from collections import Counter
s = "aabcabdscsdbbaz"
i=0
j=0
k=3
n=len(s)
ans=[]
dic={}
res=0
for i in range(1,n):
    if s[i-1]==s[i]:
        ans.append(s[i-1])
        dic= Counter(ans)
        if(len(dic)<k):
            continue
        elif(len(dic)==k):
            if(res<len(dic)):
                res=len(dic)
        else: 
            break

for j in range(i):
    if(dic[s[j]]==1):
        del[s[j]]










