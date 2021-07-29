def hammingDist(str1, str2):
    i = 0
    count = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            count += 1
        i += 1
    return count

def operation(strr,strr2,k):
    strr =list(strr)
    for i in range(len(strr)):
        ch = strr[0]
        strr.remove(strr[0])
        strr.append(ch)
        compare = hammingDist((''.join(map(str, strr))), strr2)
        if compare ==k:
            return True
            break
        else:
            continue
    return False

a="01011"
b="01110"
k=4

if(operation(a,b,k)):
    print("YES")
else:
    print("NO")

