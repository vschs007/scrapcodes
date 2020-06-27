a=[]
s=''.join(map(str,a))
inttt=int(s)
finallist=[]
inttt=inttt+1
nestring=str(inttt)
for i in range(len(nestring)):
    finallist.append(inttt%10)
    inttt=inttt//10
print(finallist[::-1])