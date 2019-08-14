class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        idx = 1
        last = nums[0]
        for i in range(1, len(nums)):
            if last != nums[i]:
                nums[idx] = nums[i]
                last = nums[i]
                idx += 1
        return idx
