def myfunc(a,x):
    low =0
    cnt=0
    high = len(a)-1
    while low <= high:
        mid = low+high //2
        if a[mid]==x:
            cnt+=1
        if a[mid]<x:
            low = mid+1
        else:
            high =mid-1
    return cnt

print(myfunc([1,2,2,2,3,4,5],2))