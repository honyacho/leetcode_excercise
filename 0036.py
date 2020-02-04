class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        st = set()
        for i in range(9)[::3]:
            for j in range(9)[::3]:
                st.clear()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != ".":
                            if board[i+k][j+l] in st:
                                return False
                            else:
                                st.add(board[i+k][j+l])
        for i in range(9):
            st.clear()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in st:
                        return False
                    else:
                        st.add(board[i][j])
        
        for i in range(9):
            st.clear()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in st:
                        return False
                    else:
                        st.add(board[j][i])
        return True
