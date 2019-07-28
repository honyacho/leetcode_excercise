class Solution:
    def lengthLongestPath(self, input: str) -> int:
        SL = input.split('\n')
        stack = []
        total = 0
        res = 0
        for st in SL:
            cnt = 0
            while st[0] == '\t':
                st = st[1:]
                cnt += 1
            le = len(st)
            while len(stack) > cnt:
                v = stack.pop()
                total -= v
            stack.append(le)
            total += le
            res = max(res, (cnt+total) if '.' in st else 0)
        return res
