n=int(input())
arr=list(map(int,input().split()))
l=len(arr)
curr=0
ans=0
while(curr<n-1):
    nextt=curr+1
    while(nextt<n-1):
        if(abs(arr[curr])>abs(arr[nextt]) or (abs(arr[curr])==abs(arr[nextt]) and abs(arr[curr])>0)):
            break
        else:
            nextt+=1
    ans+=(nextt-curr)*arr[curr]+ (pow(nextt,2)-pow(curr,2))*pow(arr[curr],2)
    curr=nextt

print(ans)