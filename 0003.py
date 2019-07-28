class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        i = 0
        j = 0
        lens = len(s)
        mp = {}

        res = 0
        while i < lens:
            is_unique = True
            for c in mp.values(): is_unique = is_unique and c <= 1
            if is_unique: res = max(j-i, res)
            
            if is_unique and j < lens:
                j += 1
                if not s[j-1] in mp: mp[s[j-1]] = 0
                mp[s[j-1]] += 1
            else:
                mp[s[i]] -= 1
                i += 1
 
        return res
