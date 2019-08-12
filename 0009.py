class Solution:
    def isPalindrome(self, x: int) -> bool:
        sti = str(x)
        i, j = 0, len(sti)-1

        res = True
        while i <= j and res:
            res = sti[i] == sti[j]
            i += 1
            j -= 1
            
        return res
