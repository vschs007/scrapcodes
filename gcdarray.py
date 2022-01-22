t = int(input())
while(t):
    arr =list(map(int,input().split()))
    l =arr[0]
    r = arr[1]
    k = arr[2]
    size = r-l+1
    if size==1:
        if l>1:
            print("YES")
        else:
            print("NO")
    elif l%2==0:
        if size%2==0:
            even = size//2
            odd = size-even
        else:
            even =size//2 +1
            odd = size - even
        if k<odd:
            print("NO")
        else:
            print("YES")
    else:
        if size%2==0:
            odd = size//2
            even = size-odd
        else:
            odd = size//2 +1
            even = size- odd
        if k<odd:
            print("NO")
        else:
            print("YES")
    t-=1