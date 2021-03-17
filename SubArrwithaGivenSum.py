def subArraySum(arr, n, s):
    res=[]
    for i in range(n-1):
        j=i+1
        csum=arr[i]
        while(j<=n):
            if(csum==s):
                res.append(i+1)
                res.append(j)
            if(csum>s or j==n):
                break
            csum=csum+arr[j]
            j+=1
    return(res[0],res[1])

a=[1,2,3,7,5]
n=5
s=12
print(subArraySum(a,n,s))