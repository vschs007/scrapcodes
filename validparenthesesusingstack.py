s="(}"
n=len(s)
arr=[len(s)]
if(s[0] in ['}',']',')']):
    print("unbalanced")
else:
    arr[0]=s[0]
for i in range(1,n):
    if s[i] in ['{','(','[']:
        arr.append(s[i])
    elif s[i] in ['}',']',')'] and len(arr)>0:
        arr.pop()

if len(arr) ==0:
    print("balanced")
else:
    print("unbalanced")
