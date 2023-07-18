# def beautiful(lst):
#     lst = sorted(list(lst))
#     for i in range(len(lst)):
#         end =lst.index('1')
#         if end >3 or end ==0:
#             return False
#         return True


arr = [4,16]
binlist=[]
start =arr[0]
end =arr[1]
while start <=end:
    startb = (bin(start).replace("0b", ""))
    print(startb)
    start+=1
res = 0
for i in range(len(binlist)):
    if beautiful(binlist[i]):
        res+=pow(int(binlist[i],2),3)

#print(res)


print(str(bin(4).replace("0b","")))

#print(beautiful('1000'))
#print(binlist)