t=int(input())
for k in range(t):
    n=int(input())
    s=input()
    lst=list(map(int,s.split(' ')))
    count=0
    for i in range(1,len(lst)-1):
        if(lst[i]>lst[i-1] and lst[i]>lst[i+1]):
            count+=1
    print("Case #"+str(k+1)+": "+str(count))
