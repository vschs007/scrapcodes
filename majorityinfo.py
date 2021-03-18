import math

A=[3,3,4 ]
sorted(A)
count=0
maxele=0
if(len(A)==1):
    print(A[0])
for i in range(len(A)):
    for j in range(0,len(A)):
        if A[i]==A[j]:
            count+=1
            if(count>=math.floor(len(A)/2)):
                maxele=(A[i])
                break
                
print(maxele)