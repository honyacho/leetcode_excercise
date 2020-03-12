class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        for num in nums:
            node = trie
            for i in range(31, -1, -1):
                d = (num >> i) & 1
                if d not in node:
                    node[d] = {}
                node = node[d]
            node = {'$'}
        res = 0
        for num in nums:
            node = trie
            cur = 0
            for i in range(31,-1,-1):
                d = (num >> i) & 1
                if (not d and (1-d) in node) or (d and (1-d) in node):
                    cur += 1 << i
                    node = node[1-d]
                else:
                    node = node[d]
            res = max(res, cur)
        return res