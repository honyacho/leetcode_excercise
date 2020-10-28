class Solution:
    def __init__(self):
        self.maxvalue = 0

    def longestValidParentheses(self, s: str) -> int:
        res = self.solve(s, 0)
        return self.maxvalue

    def solve(self, s, depth):
        res = 0
        while s[res:]:
            if s[res] == '(':
                res += 1
                res += self.solve(s[res:], depth + 1)
                if res < len(s) and s[res] == ')':
                    res += 1
                    self.maxvalue = max(self.maxvalue, res)
            else:
                if depth == 0:
                    s = s[res+1:]
                    res = 0
                else:
                    return res
        return res

    def print(self, s: str):
        print(self.longestValidParentheses(s))