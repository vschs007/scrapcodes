dp =[0]*100
dp[0]=0
dp[1]=1
for i in range(2,5):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[4])