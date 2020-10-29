class Solution:
    def dfs(self, s: str, depth: int, longest: int) -> (int, int):
        length = 0
        while s[length:]:
            if s[length] == '(':
                length += 1
                child, child_logngest = self.dfs(s[length:], depth + 1, longest)
                length += child
                longest = max(longest, child_logngest)
                if length < len(s) and s[length] == ')':
                    length += 1
                    longest = max(longest, length)
            else:
                if depth > 0:
                    return length, longest
                else:
                    s = s[length+1:]
                    length = 0
        return length, longest

    def longestValidParentheses(self, s: str) -> int:
        _, longest = self.dfs(s, 0, 0)
        return longest

    def print(self, s: str):
        print(self.longestValidParentheses(s))
