from itertools import  permutations
def iscorrect(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] % (i + 1) != 0 or (i + 1) % arr[i] != 0:
            return False
    return True

n=4
listt = []
count = 0
for i in range(1, n + 1):
    listt.append(i)


alllist = list(permutations(listt))
count = 0
for i in range(len(alllist)):

    if iscorrect(alllist[i]):
        count = count + 1
print(count)
