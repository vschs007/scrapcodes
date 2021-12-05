def isbal(s):
    count={}
    sample ="()[]?"
    for j in sample:
        count[j]=0

    for i in s:
        if i in count:
            count[i]+=1
    if ((count['('] == count[')']) and (count['('] == count[')']) and ( count['?']==0)) or ((abs(count['('] - count[')'])+abs(count['['] - count[']']))-count['?']==0):
        return True
    else:
        return False

s="[(?][??["
ans=0
for i in range(1,len(s)-1):
    left =s[:i]
    right = s[i:]
    if isbal(left) and isbal(right):
        print(left)
        print(right)
        print()
        ans+=1

print(ans)



