arr= [1, 3, 5, 6]
dc = {}
for i in range(1,7):
    dc[i]=0

for k in arr:
    dc[k]+=1

for k , v in dc.items():
    if v==0:
        print(k)