from tkinter import *
from itertools import  product

def backtrack(digits):
    if not digits: return []
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    return ["".join(num) for num in product(*[d[i] for i in digits])]
root= Tk()
root.geometry('100x100')
b =Button(root,text = "Test",command = print(backtrack("23")))
b.pack(side='top')
root.mainloop()

    # res=[]
    # mapdict ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    # def backt(i,currstr):
    #     if len(currstr) == len(digits): 
    #         res.append(currstr)
    #         return
    #     for c in mapdict[digits[i]]:
    #         backt(i+1,currstr+c)
    # if digits:
    #     backt(0,"")
    # return res


#print(backtrack("234"))
#print(list("".join(k) for k in(list(product('abc','def','ghi')))))