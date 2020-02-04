class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            cnt = 0
            lst = res[0]
            nx = ""
            for c in res:
                if c != lst:
                    nx += str(cnt)
                    nx += lst
                    cnt = 1
                    lst = c
                else:
                    cnt += 1
            nx += str(cnt)
            nx += lst
            res = nx
        return res
