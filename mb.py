def first_place (N, Q, A, Query):
    res=[]
    for i in range(N):
        if Query[i][0]=='1':
            for j in range(Query[i][1]-1,Query[i][2]-1):
                A[j]=(-1*A[j])
        else:
            for k in range(Query[i][1]-1,Query[i][2]-1):
                if A[k]<0:
                    res.append(k+1)
                else:
                    continue
    return res

