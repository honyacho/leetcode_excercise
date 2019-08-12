class Solution:
    def reverse(self, x: int) -> int:
        ma = (1 << 31) - 1
        mi = -(1 << 31)
        cand = int(str(x)[::-1]) if x >= 0 else int('-' + str(x)[1::][::-1])
        if cand > ma or cand < mi:
            return 0
        else:
            return cand
        