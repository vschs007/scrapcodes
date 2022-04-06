
def subsetsum(set,n,sum):
    if sum==0:           # very important : check fo sum will always come before the check for n because if we do
        # the other way around ,it will return false for valid cases too.
        return True
    elif n ==0:
        return False
    else:
        if set[n-1]>sum:
            return subsetsum(set,n-1,sum)
        else:
            return subsetsum(set,n-1,sum) or subsetsum(set,n-1,sum-set[n-1])

set = [5, 34, 10, 12, 5, 1]
sum = 9
n = len(set)

print(subsetsum(set,n,sum))
# dp=[[None for i in range(sum+1)]for j in range(len(set)+1)]
# for i in range(len(set)+1):
#     for j in range(sum+1):
#         if i==0 and j==0:
#             dp[i][j]=True
#         elif i==0:
#             dp[i][j]=False
#         elif j==0:
#             dp[i][j]=True
#         else:
#             if dp[i-1][j]==True:
#                 dp[i][j]=True
#             else:
#                 val = set[i-1]
#                 if j>=val:
#                     if dp[i-1][j-val]==True:
#                         dp[i][j]=True
#                     else:
#                         dp[i][j]=False
#
# print(dp[6][9])


