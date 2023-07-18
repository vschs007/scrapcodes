n, q = map(int, input().split())
a = list(map(int, input().split()))
while (q):
    qarr = list(map(int, input().split()))
    completeres =0
    id = qarr[0]
    mp =set()
    posofchange=-1
    if id == 1:
        pos=qarr[2]
        a[qarr[1]-1] = qarr[2]
    else:
        k=qarr[1]
        for i in range(k):
            completeres+=(i+1)*(k-i)
        diff = len(a[0:k])-len(set(a[0:k]))
        if diff==0:
            print(completeres)
        else:
            for i in range(k):
                if a[i] not in mp:
                    mp.add(a[i])
                else:
                    posofchange=i
                #if a.count(a[i])>1:
                 #   posofchange=i+1
                    break
            if diff==1 and posofchange==(k-1):
                print(completeres - (posofchange))
            else:
                print(completeres-((k-posofchange)*diff))
    q -= 1
