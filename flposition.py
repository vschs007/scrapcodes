arr=[5,7,7,8,8,10]
k=8
n = len(arr)
low =0
s=-1
e=-1
high =5
while(low<high):
    mid = low + high // 2
    if arr[mid] == k:
        if mid==0 or arr[mid-1]!=k:
            s=mid
        else:
            high=mid-1
    elif arr[mid]>k:
        low = mid+1

    elif arr[mid]<k:
        high=mid-1
 
