class Solution:
    def divide(self, dividend: int, divisor: int) -> int: 
        res = 0
        shift = 0
        minus = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        if dividend == -2147483648 and divisor == -1: return (1 << 31) -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend > (divisor << shift): shift += 1
        while shift >= 0:
            if dividend >= (divisor << shift):
                res += (1 << shift)
                dividend -= (divisor << shift)
            shift -= 1
        if minus:
            return -res
        else:
            return res
