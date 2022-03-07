a = [0,1,2,2,3,0,4,2]
k=2
i = 0
while(i<len(a)):
    if a[i]==k:
        a.pop(i)
        i-=1
    i+=1
print(len(a))