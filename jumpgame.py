N =4
allpair =[]
a = 1
count=0
while(a<N):
    allpair.append([a,N-a])
    a+=1

for i in range(len(allpair)):
    if allpair[i][0]+allpair[i][1] == 2* ((allpair[i][0])^(allpair[i][1])):
        count+=1
print(count)