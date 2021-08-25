def backtrack(digits):
    res=[]
    mapdict ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    def backt(i,currstr):
        if len(currstr) == len(digits):
            res.append(currstr)
            return
        for c in mapdict[digits[i]]:
            backt(i+1,currstr+c)
    if digits:
        backt(0,"")
    return res


print(backtrack(""))