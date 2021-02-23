arr=[1,2,3,4,5,6]
n=len(arr)
maxm=0
maxsofar=0
for i in range(n-1):
    for j in range(i+1,n):
        maxm= (j-i)*min(arr[i],arr[j])
        if(maxsofar<maxm):
            maxsofar=maxm

print(maxsofar)
