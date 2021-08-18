class graph:
    def __init__(self,edges):
        self.edges = edges
        self.dct ={}
        for start , end in self.edges:
            if start in self.dct:
                self.dct[start].append(end)
            else:
                self.dct[start]=[end]
       # print(self.dct)

    def getpath(self,start,end,path=[]):
        path = path +[start]

        if start == end:
            return [path]

        if start not in self.dct:
            return []

        paths = []

        for node in self.dct[start]:
            if node not in path:
                newpath = self.getpath(node,end,path)
                for p in newpath:
                    paths.append(p)
        #paths.sort()
        return paths


def MoneyPath (N, M, A):
    ans =[]
    freq={}
    graphlist=[]
    lfreq={}
    for j in range(M):
        if A[j][0] in freq:
            freq[A[j][0]]+=A[j][2]
        else:
            freq[A[j][0]] = A[j][2]

    richest = max(freq,key=freq.get)


    for j in range(M):
        if A[j][1] in lfreq:
            lfreq[A[j][1]]+=A[j][2]
        else:
            lfreq[A[j][1]]=A[j][2]
    poorest = max(lfreq, key=lfreq.get)

    for i in range(M):
        graphlist.append((A[i][0], A[i][1]))
    goobject = graph(graphlist)

    if poorest > richest:
        nss= goobject.getpath(richest, poorest)
        nss.sort(key=len)
        return " ".join(str(x) for x in nss[0][::-1])
    else:
        nss = goobject.getpath(richest, poorest)
        nss.sort(key=len)
        return " ".join(str(x) for x in nss[0][::-1])

    #return (poorest)

A= [[1,2,4],
[2 ,3, 1],
[3 ,4, 1],
[4 ,5, 3],
[3 ,5, 2]]

print(MoneyPath(5,5,A))