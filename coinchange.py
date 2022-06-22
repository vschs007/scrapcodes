import sys


def coinchange(m,v,coins):
    dp=[sys.maxsize]*(v+1)
    dp[0]=0
    for coin in coins:
        for i in range(1,v+1):
            if coin<=i:
                currmin = dp[i]
                dp[i] = min(currmin,dp[i-coin]+1)

    if dp[v]!=sys.maxsize:
        return dp[v]
    else:
        return -1

m,v = map(int,input().split())
coins = list(map(int,input().split()))
print(coinchange(m,v,coins))
