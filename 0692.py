from typing import List
import heapq
from functools import total_ordering

@total_ordering
class Freq:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

    def __gt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        else:
            return self.count > other.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        PQ = []
        count_dict = {}
        for word in words:
            if not word in count_dict:
                count_dict[word] = 1
            else:
                count_dict[word] += 1

        for word, count in count_dict.items():
            value = Freq(word, count)
            if len(PQ) < k:
                heapq.heappush(PQ, value)
            else:
                if PQ[0] < value:
                    heapq.heappop(PQ)
                    heapq.heappush(PQ, value)

        res = [heapq.heappop(PQ).word for _ in range(len(PQ))]
        res.reverse()
        return res

s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))