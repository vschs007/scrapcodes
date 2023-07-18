s = ")()())"
mxln=0
stack=[]
stack.append(-1)
for i in range(len(s)):
    if s[i]=="(":
        stack.append(i)
    else:
        stack.pop()
        if len(stack)==0:
            stack.append(i)
        ln = i-stack[-1]
        mxln = max(ln,mxln)
print(mxln)