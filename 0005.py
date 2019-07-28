class Solution:
    def impl(self, s, i, j):
        if j < len(s) and i >= 1:
            if s[i-1] == s[j]:
                return self.impl(s, i-1, j+1)
            else:
                return (i, j)
        else:
            return (i, j)

        
    def longestPalindrome(self, s: str) -> str:
        maxij = (0, 0)
        for i in range(len(s)):
            i1, j1 = self.impl(s, i, i+1)
            if j1-i1 > maxij[1]-maxij[0]:
                maxij = (i1,j1)
            i2, j2 = self.impl(s, i, i)
            if j2-i2 > maxij[1]-maxij[0]:
                maxij = (i2,j2)
        return s[maxij[0]:maxij[1]]
