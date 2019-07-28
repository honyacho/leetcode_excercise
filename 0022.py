class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = self
        return list(filter(self.is_valid, self.gen(n*2)))
        
    def gen(self, n2):
        if n2 == 0: return [""]
        res = []
        for st in self.gen(n2-2):
            res.append(st+"()")
            res.append(st+")(")
            res.append(st+"((")
            res.append(st+"))")
        return res
    
    def is_valid(self, st):
        lft = 0
        rgt = 0
        for i in range(len(st)):
            lft += '(' == st[i]
            rgt += '(' != st[i]
            if rgt > lft:
                return False
        return lft == rgt
