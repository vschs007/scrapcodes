def acmTeam(topic):
    d = []
    resdic = {}
    m = 0
    for t in topic:
        temp = set()
        for i in range(len(t)):
            if t[i]=='1':
                temp.add(i)
        d.append(temp.copy())
    # print(d)
    for i in range(len(d)-1):
        for j in range(i+1,len(d)):
            l = len(d[i].union(d[j]))
            m = max(m,l)
            resdic[l]=resdic.get(l,0)+1
    return [m,resdic[m]]

topic = ['10101','11100','11010','00101']
print(acmTeam(topic))