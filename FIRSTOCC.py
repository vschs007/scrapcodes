arr=[1, 3, 5, 5, 5, 5, 7, 123, 125]
n=len(arr)
k=125
low = 0
left=-1
right=-1
high = n-1
while(low<=high):
    mid = (low+high)//2
    if k ==arr[mid]:
        if mid-1!=0 and k==arr[mid-1]:
            high=mid-1
        else:
            left = mid
            break
    elif arr[mid]<k:
        low=mid+1
    else:
        high = mid-1

if left>=0:
    low = left
high=n-1
while(low<=high):
    mid=(low+high)//2
    if arr[mid]==k:
        if mid+1<n and k==arr[mid+1]:
            low=mid+1
        else:
            right =mid
            break
    elif arr[mid]>k:
        high=mid-1
print(left, right)



