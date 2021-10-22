s = []
c = set()
def isord(str):
    arr=[]
    for i in range(len(str)):
        temp =ord(str[i])
        temp2 = temp - 97
        arr.append(chr(122-temp2))
    return "".join(arr)

count = len(s)
for i in range(len(s)):
    if s[i] not in c:
        if isord(s[i]) in s:
            count-=1
            c.add(s[i])
            c.add(isord(s[i]))
print(count)