arr= [5,3,11,2,3,]

s=set()
for i in range(len(arr)):
    if arr[i] in s:
        print(arr[i])
        break
    else:
        s.add(arr[i])














# import time
#
# def dec(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func(*args,**kwargs)
#         end = time.time()
#         print((end-start)*1000)
#         return res
#     return wrapper
#
# @dec
# def calsquare(arr):
#     result = [x*x for x in arr]
#     return result
#
#
# array =range(1,10000000)
# output = calsquare(array)