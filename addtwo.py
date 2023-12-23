class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (divisor*dividend)<0

        dividend = abs(dividend)
        divisor = abs(divisor)
        res = len(range(0,dividend-divisor+1,divisor))

        if sign:
            res= -res
        else:
            res = res
        #this part is painful

        return min(max(res,-(2**31)),(2**31 -1))