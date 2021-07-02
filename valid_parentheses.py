s = "}}}}}}}}}}}}}}"
#print(len(s))
arr=[]
for i in range(len(s)):
    if(s[i]=="(" or s[i]=="{" or s[i]=="["):
        arr.append(s[i])
    if (s[i] == ")"):
        if(len(arr)==0 or arr[-1]!="("):
            arr.append(s[i])
        elif(arr[-1]=="("):
            arr.pop()



    if (s[i] == "}"):
        if (len(arr) == 0 or arr[-1]!="{"):
            arr.append(s[i])
        elif (arr[-1] == "{"):
            arr.pop()


    if (s[i] == "]"):
        if (len(arr) == 0 or arr[-1]!="["):
            arr.append(s[i])
        elif (arr[-1] == "["):
            arr.pop()
    print(arr)

#print(arr)
if(len(arr)==0):
    print("True")
else:
    print("False")
