# import math
# t =int(input())
# while(t):
#     n = int(input())
#     arr= list(map(int,input().split()))
#     summ = sum(arr[0:])
#     minn = summ//n
#     maxx = math.ceil(summ/n)
#     print(maxx-minn)
#     t-=1

t = int(input())
while (t):
    n = int(input())
    arr = list(map(int, input().split()))
    newarr = sorted(arr)
    print((newarr[-1] - newarr[0]) * newarr[-2])
    t -= 1
