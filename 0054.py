class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix: return res
        M,N=len(matrix),len(matrix[0])
        cnt, i, j = 0, 0, 0
        min_i, max_i, min_j, max_j = 0, M-1, 0, N-1
        size = M*N

        dir_x = 1 if len(matrix[0]) > 1 else 0
        dir_y = 1 if len(matrix[0]) == 1 else 0
        for cnt in range(size):
            res.append(matrix[i][j])
            i += dir_y
            j += dir_x
            if i == min_i and j == max_j and dir_y != 1 and min_i != max_i:
                min_i += 1
                dir_x, dir_y = 0, 1
            if i == max_i and j == max_j and dir_x != -1 and min_j != max_j:
                max_j -= 1
                dir_x, dir_y = -1, 0
            if j == min_j and i == max_i and dir_y != -1 and min_i != max_i:
                max_i -= 1
                dir_x, dir_y = 0, -1
            if j == min_j and i == min_i and dir_x != 1 and min_j != max_j:
                min_j += 1
                dir_x, dir_y = 1, 0

        return res
