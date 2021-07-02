
#hotstar interview,
















import sys
arr = [1, 3, 4, 7, 10]
x = 15
left = 0
diff = sys.maxsize
right = len(arr)-1
while(right>left):
    sumsofar = arr[left]+arr[right]
    dif = abs(x-(arr[left]+arr[right]))
    if(dif<diff):
        diff = dif
        l = arr[left]
        r = arr[right]

    if(sumsofar > x):
        right-=1
    elif sumsofar < x:
        left+=1
print(l,r)