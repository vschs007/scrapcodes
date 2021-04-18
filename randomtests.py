from collections import  Counter
word='110111001111'
count=0
k=1
wsorted=sorted(word)
arr=[]
diffarr=[]
arrformaxlen=[]
#print(max(Counter(word),key=Counter(word).get))
maxchar=(max(Counter(word),key=Counter(word).get))
#print(maxchar)
for i in range(len(wsorted)):
    if wsorted[i]==maxchar:
        arrformaxlen.append(i)
        break
for i in range(len(wsorted)-1,0,-1):
    if wsorted[i]==maxchar:
        arrformaxlen.append(i)
        break
for i in range(len(word)):
    if(word[i]==maxchar):
        arr.append(i)
        break
for i in range(len(word)-1,0,-1):
    if(word[i]==maxchar):
        arr.append(i)
        break
for j in range(arr[0],arr[-1]):
    if word[j]!=wsorted[j]:
        diffarr.append(j)
        count=count+1

#print(count)
#print(diffarr)
diffarr.remove(diffarr[-1])
#print(diffarr)
#print(arr)
#print(arrformaxlen)
lenofmaxfrequenctchar=arrformaxlen[-1]-arrformaxlen[0]+1
#print(lenofmaxfrequenctchar)
maxswappossible=count-1
#print(maxswappossible)
if(k==maxswappossible):
    print(lenofmaxfrequenctchar)
if k < maxswappossible:
    print(diffarr[k])
if k> maxswappossible:
    print(lenofmaxfrequenctchar)

