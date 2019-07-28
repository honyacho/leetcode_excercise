class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cnt = 0
        prefix = ''
        while strs and len(strs[0]) > cnt:
            prefix += strs[0][cnt]
            for st in strs[1:]:
                if len(st) > cnt:
                    if prefix[cnt] != st[cnt]:
                        return prefix[:-1]
                else:
                    return prefix[:-1]
            cnt += 1
        return prefix
