import re


class Solution:
    def procDigit(self, s, ten, five, one, scale) -> (str, int):
        cnt = 0
        while s and s[0] == ten:
            cnt += 10*scale
            s = s[1:]
        
        if s and s[0:2] == (one+ten):
            cnt += 9*scale
            s = s[2:]

        tester = re.compile('^({}?){}({}{})'.format(one, five, one, '{0,3}'))
        match_obj = tester.match(s)
        if match_obj:
            cnt += (5*scale - len(match_obj[1])*scale + len(match_obj[2])*scale)
            s = s[len(match_obj[0]):]
        
        return s, cnt


    def romanToInt(self, s: str) -> int:
        cnt = 0
        s, cnt1 = self.procDigit(s, 'M', 'D', 'C', 100)
        cnt += cnt1
        s, cnt2 = self.procDigit(s, 'C', 'L', 'X', 10)
        cnt += cnt2
        s, cnt3 = self.procDigit(s, 'X', 'V', 'I', 1)
        cnt += cnt3

        while s and s[0] == 'I':
            cnt += 1
            s = s[1:]

        return cnt
