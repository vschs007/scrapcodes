import  itertools
def bitwise(arr,k):
    n=len(arr)
    count=0
    for i in range(n-1):
            if(arr[i]^arr[i+1] == k):
                count=count+1
            else:
                break
    if count==len(arr)-1:
        return True
    else:
        return False


def printSubsequences(arr,k):
    newarr=[]
    maxx=0
    for r in range(1,len(arr)+1):
        for c in itertools.combinations(arr,r):
            if(bitwise(c,k)):
                newarr.append(c)
    for i in range(len(newarr)):
        currlen = len(newarr[i])
        maxx=max(currlen,maxx)
    if(maxx>=2):
        return maxx
    else:
        return 0


t=int(input())
for i in range(t):
    size,k =map(int,input().strip().split())
    arr= list(map(int,input().strip().split()))
    print(printSubsequences(arr,k))



