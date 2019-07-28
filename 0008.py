import re

class Solution:
    def myAtoi(self, st: str) -> int:
        matcher = re.compile('^\s*([+-]?)0*([\d]+)')
        match_obj = matcher.match(st)
        if not match_obj: return 0
        
        ex_str = (match_obj[1] or '+') + match_obj[2]
        if ex_str[0] == '+':
            ex_str = ex_str[1:]
        
        if ex_str[0] == '-':
            if len(ex_str) > 11:
                return -2147483648                
            if str(-(1 << 31)) < '-0000000000'[:12-len(ex_str)] + ex_str[1:]:
                print('-0000000000'[:11-len(ex_str)] + ex_str[1:])
                return -2147483648
        else:
            if len(ex_str) > 10:
                return 2147483647
            if '0000000000'[:10-len(ex_str)] + ex_str > str((1 << 31)-1):
                return 2147483647

        return int(ex_str)
