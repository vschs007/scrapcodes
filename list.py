def max_value (n, k):
    #res = 0
    ans = []
    if k > int(n):
        return int(n)
    for i in range(1,len(n)+1):
        res = 0
        newstr = n[:i-1] + n[i:]
        newarr=newstr[::-1]
        for j in range(0,len(newarr)):
            res+=(int(newarr[j])*pow(10,j))%k
        res = res%k
        #res=res%k
        ans.append(res)
    return max(ans)

n ='123324324'
nnew = n[::-1]
#print(nnew)
k=2312
print(max_value(n,k))
#ans=0
# for i in range(len(n)):
#     ans+= (int(nnew[i])*pow(10,i))%k
# print(ans%k)
# print(int(n)%k)


