class Solution:
    def dfs(self, s: str, depth: int, longest: int) -> (int, int):
        length = 0
        while s:
            if s[0] == '(':
                res, child_longest = self.dfs(s[1:], depth + 1, longest)
                s = s[res:]
                longest = max(longest, child_longest)
                print(res)
                length += res
                longest = max(length, longest)
            else:
                if depth == 0:
                    s = s[1:]
                else:
                    return length + 2, longest
        return length, longest

    def longestValidParentheses(self, s: str) -> int:
        _, longest = self.dfs(s, 0, 0)
        return longest
