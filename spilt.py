def suffixCount (N, A, Q, B):
    # Write your code her
    res=[]
    for i in range(Q):
        cnt=0
        tmp = B[i]
        for k in A:
            if tmp in k:
                cnt+=1
        res.append(cnt)
    print(res)


N = int(input())
A = []
for _ in range(N):
    A.append(input())
Q = int(input())
B = []
for _ in range(Q):
    B.append(input())

out_ = suffixCount(N, A, Q, B)
print (' '.join(map(str, out_)))