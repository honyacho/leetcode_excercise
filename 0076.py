class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 1
        min_l = 0
        min_r = 10**18

        MP = {}
        for i in t:
            if not i in MP: MP[i] = 0
            MP[i] -= 1

        if s[0] in MP:
            MP[s[0]] += 1

        while left < right:
            ok = True
            for cnt in MP.values():
                ok = ok and cnt >= 0

            if not ok and right < len(s):
                if s[right] in MP: MP[s[right]] += 1
                right += 1
            else:
                if ok and min_r - min_l > right - left:
                    min_r, min_l = right, left

                if s[left] in MP: MP[s[left]] -= 1
                left += 1

        return s[min_l:min_r] if min_r - min_l <= len(s) else ""
