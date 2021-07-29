def strength(x):
    if x<=2:
        return 1
    elif x==3:
        return 2
    # elif x==4:
    #     return 3
    # elif x==5:
    #     return 2
    # elif x==6:
    #     return 4
    else:
        for i in range(2,x):
            if x%i!=0:
                return i
                break
            else:
                continue
res=0
for i in range(108,110):
    res+=strength(i)
print(res)

