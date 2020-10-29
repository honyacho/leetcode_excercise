class Solution:
    def search(self, nums: list, target: int) -> int:
        if not nums: return -1
        lo, hi = 0, len(nums)-1
        L = len(nums)
        while lo != hi:
            mid = (lo+hi)//2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid+1
        zero = lo
        lo, hi = 0, len(nums)-1

        while lo != hi:
            mid = (lo+hi)//2
            if target > nums[(mid+zero)%L]:
                lo = mid+1
            else:
                hi = mid
        # print(zero, lo)

        if nums[(lo+zero)%L] == target:
            return (lo+zero)%L
        else:
            return -1
