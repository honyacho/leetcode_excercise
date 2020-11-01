from typing import List

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.tree = {}
        self.current = []
        for sentence, count in zip(sentences, times):
            self.add(sentence, count)

    def add(self, sentence: str, count: int):
        node = self.tree
        for c in sentence:
            if not c in node:
                node[c] = {}
            node = node[c]
        if not "count" in node: node["count"] = 0
        node["count"] -= count

    def search(self, node: map, input_chars: List[str], result: List[str]) -> List[str]:
        if not node: return []
        for chara, next_node in node.items():
            if chara != "count":
                input_chars.append(chara)
                self.search(next_node, input_chars, result)
                input_chars.pop()
            else:
                result.append((next_node, "".join(input_chars)))
        return result

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add("".join(self.current), 1)
            self.current.clear()
            return []
        else:
            self.current.append(c)
            node = self.tree
            for c in self.current:
                if node:
                    node = node.get(c)
            res = self.search(node, self.current, [])
            res.sort()
            return list(map(lambda x: x[1], res))[:3]


# acs = AutocompleteSystem(["i love you","island","iroman","i love leetcode"], [5,3,2,2])
# print(acs.tree)
# print(acs.input("i"))
# print(acs.input(" "))
# print(acs.input("a"))
# print(acs.input("#"))
# print(acs.input("i"))
# print(acs.input(" "))