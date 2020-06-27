arr=[]
x=905
i =1
res=1
while(res <= x):
    i+=1
    res = i*i

print(i-1)



class Solution:
    def mySqrt(self, x: int) -> int:
        if (x < 0):
            return False
        if (x == 0 or x == 1):
            return x
        res = 1
        i = 1
        while (res <= x):
            i += 1
            res = i * i
        return i - 1










