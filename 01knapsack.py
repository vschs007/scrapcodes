def knapsack(w,c,capacity,n):
    if n==0 or capacity==0:
        return 0
    elif w[n-1]<=capacity:
        return max(c[n-1]+knapsack(w,c,capacity-w[n-1],n-1),knapsack(w,c,capacity,n-1))
    else:
        return knapsack(w,c,capacity,n-1)

weight=[2,4,6,8,2,4,8]
cost=[4,6,2,3,1,8,7]
capacity = 10

n= len(weight)
print(knapsack(weight,cost,capacity,n))


