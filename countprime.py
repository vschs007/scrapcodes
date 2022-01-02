
n=10
arr = [True]*n
arr[1] = False
arr[0]=False
for i in range(2,int(pow(n,1/2))+1):
    j=i
    if arr[i]:
        while i*j<n:
            arr[i*j]=False
            j+=1
        j=2

print(arr.count(True))

