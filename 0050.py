MEMO = {}

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        elif n == 1: return x
        elif n == -1: return 1/x

        if (x, n) in MEMO: return MEMO[(x,n)]
        half = n // 2

        res = 1
        if n%2 == 0:
            res = self.myPow(x, half)*self.myPow(x, half)      
        else:
            res = self.myPow(x, half)*self.myPow(x, half)*x
        MEMO[(x, n)] = res
        return res
