# from collections import deque

class Trie:
    def __init__(self):
        self.isWord = False
        self.children = {}
    
    def add(self, s):
        if not s:
            self.isWord = True
            return
        if not s[0] in self.children:
            self.children[s[0]] = Trie()
        self.children[s[0]].add(s[1:])

    def check(self, s):
        if not s: return self.isWord

        if s[0] in self.children:
            return self.children[s[0]].check(s[1:])
        else:
            return False
    
    def __str__(self):
        mp = {}
        for k,v in self.children.items():
            mp[k] = str(v)
            if v.isWord:
                mp[k] += 'isWord'
        return str(mp).replace('\\', '')


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        st = set([0])
        trie = Trie()
        maxlen = 0
        for wd in wordDict:
            maxlen = max(maxlen, len(wd))
            trie.add(wd)
    
        res = False
        while st:
            ptr = st.pop()
            if ptr == N:
                return True

            for i in range(ptr+1, N+1):
                if trie.check(s[ptr:i]):
                    st.add(i)
                else:
                    if i-ptr > maxlen:
                        break

        return False
