class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)
        # bisect_left
        while lo != hi:
            mid = (lo + hi)//2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        res_L = lo
        
        lo, hi = 0, len(nums)
        while lo != hi:
            mid = (lo + hi)//2
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        res_R = lo
        if res_L == res_R:
            return [-1, -1]
        else:
            return [res_L, res_R-1]
