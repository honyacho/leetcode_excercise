class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ma = -1
        tgt = -1
        L = len(nums)
        for i in reversed(range(len(nums))):
            if nums[i] >= ma:
                ma = nums[i]
            else:
                tgt = i
                break
        print("ma tgt: {} {}".format(ma, tgt))
    
        if tgt == -1:
            nums.reverse()
        else:
            mi = 10000000000
            idx = 0
            for i in range(tgt+1, len(nums)):
                if mi >= nums[i] and nums[i] > nums[tgt]:
                    mi = nums[i]
                    idx = i
                # elif mi >= nums[i] and nums[i] > nums[tgt]:
                #     continue
                else:
                    break
            print("idx {} mi {}".format(idx, mi))
            nums[idx], nums[tgt] = nums[tgt], nums[idx]
            print(nums)
            left = tgt+1
            right = L-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
