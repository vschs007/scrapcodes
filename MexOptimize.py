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


