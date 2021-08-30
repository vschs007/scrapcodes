ar = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
#ans =2

visited = {}
for i in range(len(ar)):
    if ar[i] not in visited:
        visited[ar[i]]=1
    else:
        visited[ar[i]]+=1
for key,val in visited.items():
    if val ==1:
        print(key)
