class Solution:
    def dfs(self, s: str, depth: int, longest: int) -> (int, int, bool):
        length = 0
        while s:
            if s[0] == '(':
                res, child_longest, end = self.dfs(s[1:], depth + 1, longest)
                if res+1 < len(s) and s[res+1] == ')':
                    s = s[res+2:]
                    length += res + 2
                    longest = max(longest, length)
                else:
                    s = s[res+1:]
                    longest = max(longest, res)
                    # length = 0
                if end:
                    return res, longest, True
            else:
                if depth > 0:
                    return length, longest, False
                else:
                    s = s[1:]
                    length = 0
        return length, longest, True

    def longestValidParentheses(self, s: str) -> int:
        _, longest, _ = self.dfs(s, 0, 0)
        return longest

    def print(self, s: str):
        print(self.longestValidParentheses(s))

sol = Solution()
sol.print("))(()))))(((((()(()))(()((((()(((((((())())()()(())))))))))")
sol.print("))(()))))(((((()(()))(()((((()(((((((())())()()(())))))))))(((()(()(((())))())((()))(((()((((()((())()()()")

sol.print("(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((")
