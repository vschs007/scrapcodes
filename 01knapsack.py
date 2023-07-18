
def knapsack(w,c,capacity,n):
    if n==0 or capacity==0:
        return 0
    elif t[n][n]!=-1:
        return t[n][n]
    elif w[n-1]<=capacity:
      #  return  max(c[n-1]+knapsack(w,c,capacity-w[n-1],n-1),knapsack(w,c,capacity,n-1))
        t[n][n]= max(c[n-1]+knapsack(w,c,capacity-w[n-1],n-1),knapsack(w,c,capacity,n-1))
    else:
        #return knapsack(w,c,capacity,n-1)
        t[n][n]= knapsack(w,c,capacity,n-1)
    return t[n][n]

weight=[20, 10, 40, 30]
cost=[40, 100, 50, 60]
capacity = 60
n=len(weight)
global t
t=[[-1]*(n+1)]*(n+1)
#print(t)
print(knapsack(weight,cost,capacity,n))


