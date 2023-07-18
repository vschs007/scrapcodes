# arr = [3,5,1,6,8,2]
# first = -1
# second =-1
#
# # just initialisations
#
# #looping through the elements
# for i in range(len(arr)): #len method gives the size of array
#     if arr[i]>first:                  # this to update the higest if we encounter any number greater than current highest
#         second = first
#         first  = arr[i]
#     elif arr[i]<first and arr[i]>second:
#         second = arr[i]                           # this for the case where number in array is greater than second highest but less than higest so far
#
# print(second)
#
#
def timeit(func):
    def wrapper(*args,**kwargs):
        start =""
        result =  func(*args,**kwargs)
        end =""


