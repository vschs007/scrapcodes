s="how many dozens,does make a dozen ? 13"

lst = list(map(str,s.replace(" ",",").split(",")))

print(lst)
cnt=0
for k in lst:
    if k !='?' and type(k)!=int:
        cnt+=1


print(cnt)
