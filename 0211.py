class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        res = self._addWord(word, self.root)
        return res

    def _addWord(self, word, node):
        if word == '':
            node["end"] = True
        else:
            if not word[0] in node: node[word[0]] = {}
            self._addWord(word[1:], node[word[0]])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(word, self.root)


    def _search(self, word, node):
        if word == '':
            return "end" in node
        elif word[0] == '.':
            res = False
            for k in node.keys():
                if k != 'end':
                    res = res or self._search(word[1:], node[k])
            return res
        else:
            if word[0] in node:
                return self._search(word[1:], node[word[0]])
            else:
                return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)