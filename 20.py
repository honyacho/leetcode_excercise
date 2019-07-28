class Solution:
    def isValidImpl(self, s: str):
        while s:
            try:
                if s[0] == '(':
                    corr, s = self.isValidImpl(s[1:])
                    if corr != ')':
                        return False
                    else:
                        continue
                if s[0] == '[':
                    corr, s = self.isValidImpl(s[1:])
                    if corr != ']':
                        return False
                    else:
                        continue
                if s[0] == '{':
                    corr, s = self.isValidImpl(s[1:])
                    if corr != '}':
                        return False
                    else:
                        continue
                if s[0] == ')' or s[0] == ']' or s[0] == '}':
                    return (s[0], s[1:])
            except:
                return False
        if s == '':
            return True

    def isValid(self, s: str) -> bool:
        return True == self.isValidImpl(s)
