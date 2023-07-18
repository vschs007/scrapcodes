templist = list(map(int,input().split(sep=",")))    #taking comma seperate input and covert to list
#finding the index of largest number
    maxele_index = 0
for i in range(len(templist)):
    if templist[i]>templist[maxele_index]:
        maxele_index = i
# now at index maxele_index, we have our max element ,
templist[maxele_index]+=5

print(templist)
