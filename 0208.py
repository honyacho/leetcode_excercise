class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self._insert(word, self.root)

    def _insert(self, word, node):
        if word == '':
            node["end"] = True
        else:
            if not word[0] in node: node[word[0]] = {}
            self._insert(word[1:], node[word[0]])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self._search(word, self.root)

    def _search(self, word, node, isStartsWith = False):
        if word == '':
            return ("end" in node or isStartsWith)
        else:
            if not word[0] in node:
                return False
            return self._search(word[1:], node[word[0]], isStartsWith)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._search(prefix, self.root, isStartsWith = True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)