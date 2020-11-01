from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        pile_length = len(piles)
        results = [[(0,0) for _ in range(pile_length+1)] for _ in range(pile_length+1)]

        for length in range(1, pile_length+1):
            for i in range(0, pile_length - length + 1):
                first, second = 0, 0

                # 1st round
                firstA, secondA = results[i][i+length-1]
                firstA, secondA = secondA, firstA

                firstA += piles[i+length-1]
                first, second = firstA, secondA

                # 2nd round
                firstB, secondB = results[i+1][i+length]
                firstB, secondB = secondB, firstB

                firstB += piles[i]
                if first < firstB:
                    first, second = firstB, secondB

                results[i][i+length] = (first, second)

        fst, snd = results[0][pile_length]
        return fst > snd
