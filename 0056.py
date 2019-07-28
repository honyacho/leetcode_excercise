class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        
        res = []
        intervals.sort()
        tl, tr = intervals[0]

        for i, j in intervals[1:]:
            if i <= tr:
                tr = max(tr,j)
            else:
                res.append([tl, tr])
                tl, tr = i, j
        res.append([tl, tr])
        return res
