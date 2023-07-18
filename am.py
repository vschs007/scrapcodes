def isord(r):
    arr=[]
    for i in range(len(r)):
        temp = ord(r[i])
        temp2 = temp - 97
        arr.append(chr(122-temp2))
    return "".join(arr)

def findMessages (N, A):
    c =set()
    count =len(A)
    for i in range(len(A)):
        if A[i] not in c:
            if isord(A[i]) in A:
                count-=1
                c.add[A[i]]
                c.add(isord(A[i]))
    return count

N = int(input())
B = input()
A = B.split(" ")[0:]

out_ = findMessages(N, A)
print (out_)
print(A)