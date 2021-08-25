from itertools import  combinations ,permutations
def custompermut(digits,res):
    if len(digits)==1:
        return mapdict[digits]
    else:
        left = [l for l in mapdict[digits[0]]]
        right = [ k for k in mapdict[digits[1:]]]
        for i in range(len(right)):
            for j in range(len(left)):
                res.append(left[j]+right[i])
        custompermut(right,res)
    return  res


num = "23"
mapdict ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

print(custompermut(num,res=[]))