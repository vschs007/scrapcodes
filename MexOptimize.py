arr = [2,3]
c =set()
for i in range(max(arr)+1):
    c.add(i)
for i in range(len(arr)):
    try:
        c.remove(arr[i])
    except:
        continue


print(list(c)[0])
# for i in range(0,len(arr)):
#     if arr[i] in list(c):
#         c.remove(arr[i])
#     res =list(c)[0]
#
# for j in range(i+1,len(arr)):
#     if arr[j] in list(c):
#         c.remove(arr[j])
#     res2 = list(c)[0]

