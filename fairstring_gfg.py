def fairone(arr,cost):
    costzero = 0
    costone = 0
    if arr[0]=='0':
        for j in range(1,len(arr),2):
            if arr[j]!='1':
                arr[j]='1'
                costzero+=cost[j]
            else:
                continue
    elif arr[0]=='1':
        for j in range(1,len(arr),2):
            arr[j]='0'
            costone+=cost[j]
    return max(costzero,costone)


def fairtwo(arr,cost):
    costzero = 0
    costone = 0
    if arr[0]=='1':
        for j in range(1,len(arr),4):
            if arr[j]!='1':
                arr[j]='1'
                costone+=cost[j]
            elif arr[j-1]!='1':
                arr[j-1]='1'
                costone+=cost[j-1]
            else:
                continue
    elif arr[0]=='0':
        for j in range(1,len(arr),4):
            if arr[j]!='0':
                arr[j]='0'
                costzero+=cost[j]
            elif arr[j-1]!='0':
                arr[j-1]='0'
                costzero+=cost[j-1]
            else:
                continue
    return max(costzero,costone)


s="001000000"
s=list(s)
n = 4
c=[1,0,4,0,3,4,3,4,3]

print(min(fairtwo(s,c),fairtwo(s,c)))

