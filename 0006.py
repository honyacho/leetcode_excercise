from io import StringIO


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s: return s
        if numRows == 1: return s
        if numRows == 2: return s[::2] + s[1::2]

        io = StringIO()
        div = 2*numRows-2
        io.write(s[::div])
        for i in range(1, numRows-1):
            jig = s[i::div]
            zag = s[div-i::div]

            for i in range(len(s)//div+1):
                if i < len(jig): io.write(jig[i])
                if i < len(zag): io.write(zag[i])

        io.write(s[numRows-1::div])
        return io.getvalue()
