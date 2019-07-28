class Solution:
    def acc(self, s, x, y, rows):
        return s[rows*y+x]

    def convert(self, s: str, numRows: int) -> str:
        width = len(s) if numRows == 1 else s.index('\n')
        for i in range(width):
            if i % numRows == 1 or i % numRows == numRows-1:
                for j in range(numRows):
                    print(self.acc(s,i,j,numRows), end='')
