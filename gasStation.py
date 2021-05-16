gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
sp=0
curr=0
gasremains=0
for i in range(len(gas)):
    gasremains+=gas[i]-cost[i]
    curr+=gas[i]-cost[i]
    if(curr<0):
        sp=sp+1
        curr=0

if(gasremains>=0):
    print(sp)
else:
    print(-1)






