class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i]*(j-i))
                i += 1
            else:
                res = max(res, height[j]*(j-i))
                j -= 1

        return res
