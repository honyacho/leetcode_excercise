class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        for m in range(M):
            for n in range(N):
                cnt = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if not (i == j and i == 0) and m+i >= 0 and m+i < M and n+j >= 0 and n+j < N and (board[m+i][n+j] == 1 or board[m+i][n+j] == -2):
                            cnt+=1
                # print("1:{}".format(cnt))
                if board[m][n] == 0:
                    if cnt == 3:
                        board[m][n] = -1
                else:
                    if cnt < 2 or cnt > 3:
                        board[m][n] = -2


        for m in range(M):
            for n in range(N):
                if board[m][n] == -1:
                    board[m][n] = 1
                if board[m][n] == -2:
                    board[m][n] = 0
