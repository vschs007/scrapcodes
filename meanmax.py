t= int(input())
while(t):
    n= int(input())
    arr= list(map(int,input().split()))
    arr= sorted(arr,reverse=True)
    sum1 = sum(arr)
    sum2= arr[0]
    ans = (sum1-sum2)/(n-1)
    ans+=sum2
    print(format(ans,'.6f'))
    t-=1