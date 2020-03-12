class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = self.buildTrie(words)

        diffs = [(1,0),(-1,0),(0,1),(0,-1)]
        results = set()
        def withinBound(i,j):
            return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])

        def dfs(i, j, node, visited, trail):
            if '$' in node: results.add(trail)

            for di, dj in diffs:
                ii, jj = i+di, j+dj
                ok = False
                if not ok and withinBound(ii,jj) and board[ii][jj] in node and not (ii, jj) in visited:
                    visited.add((ii, jj))
                    dfs(ii, jj, node[board[ii][jj]], visited, trail + board[ii][jj])
                    visited.remove((ii,jj))

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited.add((i,j))
                if board[i][j] in tree:
                    dfs(i, j, tree[board[i][j]], visited, board[i][j])
                visited.remove((i,j))
        return list(results)

    def buildTrie(self, words):
        trie = {}
        head = trie

        for word in words:
            for letter in word:
                if letter not in trie:
                    trie[letter] = {}
                trie = trie[letter]
            trie['$'] = {}
            trie = head
        return trie