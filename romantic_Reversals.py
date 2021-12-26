t = int(input())
while(t):
    ans=""
    sz,k = map(int,input().split())
    s=input()
    i=0
    j=k-1
    while(i<j):
        ans+=s[i]
        ans+=s[j]
        i+=1
        j-=1
    if i==j:
        ans+=s[i]

    ans =ans[::-1]
    print(ans+s[k:])
    t-=1




