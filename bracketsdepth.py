s="12112212112122112122"

arr=[]
count=0
start=0
end=0
resarr=[]
for i in range(0,len(s)):
    if(s[i]=="1"):
        arr.append(s[i])
        count+=1
    elif(s[i]=="2"):
        arr.pop()
        count+=1
        if(len(arr)==0):
            start=i
            resarr.append(arr)
            #prevcount=count
            count=0


print(resarr)
Keymax = max(resarr, key=resarr.get)
print(Keymax)




