n =12
dp=[None]*(n+1)
dp[0]= 0
dp[1]=1
for i in range(2,n+1):
    mn = 99999
    j=1
    while(j*j<=i):
        rem = i -(j*j)
        if dp[rem]<mn:
            mn = dp[rem]
        j+=1
    dp[i] = mn+1
print(dp[n])
print(dp)