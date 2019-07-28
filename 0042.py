class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1 or len(height) == 0:
            return 0
        height.insert(0, 0)
        height.append(0)
        lft = 0
        rgt = len(height)
        cur = 0
        res = 0
        while lft != rgt:
            print(lft, rgt)
            if height[lft+1] <= cur:
                lft += 1
            if height[rgt-1] <= cur:
                rgt -= 1 
            if rgt <= lft:
                break

            if height[lft+1] > cur and \
                height[rgt-1] > cur:
                ne = min(height[lft+1], height[rgt-1])
                res += (ne - cur)*(rgt - lft - 1)
                cur = ne
        # print(res)
        # print(sum(height)) 
        return res - sum(height)
