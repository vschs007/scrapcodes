# def binarysearch(arr,low,high,key):
#     while high >=low:
#         mid = high+low//2
#
#         if key == arr[mid]:
#             return mid
#
#         elif key > arr[mid]:
#             return binarysearch(arr,low,mid-1,key)
#
#         elif key < arr[mid]:
#             return  binarysearch(arr,mid+1,high,key)
#
# arr=[1,2,3,4,5,6,7,8,9,10]
# key = 10
# low = 0
# high =len(arr)-1
# print(binarysearch(arr,low,high,key))

# def bf(arr,key):
#     low = 0
#     high = len(arr)-1
#     mid=0
#     while(low<=high):
#         mid = low+high//2
#         if key == arr[mid]:
#             return mid
#         elif key>arr[mid]:
#             low = mid+1
#         elif key <arr[mid]:
#             high = mid-1
#     return -1
def bf(arr,key):
    low = 0
    high = len(arr)-1
    mid=0
    while(low<=high):
        mid = low+high//2
        if key == arr[mid]:
            return mid
        elif key>arr[mid] and arr[mid]>arr[low]:
            low = mid+1
        elif key <arr[mid]:
            high = mid-1
    return -1





arr=[5, 6, 7, 8, 9, 10, 1, 2, 3]
print(bf(arr,10))