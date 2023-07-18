a = [40,20,20,10]
b=[40,5,30]

a= sorted(a,reverse= True)
b= sorted(b,reverse= True)
cnt=0
for i in a:
    j=0
    while(len(b)>0):
        if j<len(b):
            if b[j]<=i:
                cnt+=1
                b.remove(b[j])
                break
            else:
                j+=1
        else:
            break


print(cnt)
