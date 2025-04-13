nums = [1,1,1,2,2,3]

hashmap ={}

for k in nums:
    if k not in hashmap:
        hashmap[k]=1
    else:
        hashmap[k]+=1


for k,v in hashmap.items():
    print(k,v)

