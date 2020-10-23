class Node:
    def __init__(self, value, upper, tail):
        self.value = value
        self.tail = tail
        self.upper = upper

    def __str__(self):
        return "Node({},{},{})".format(self.value, "upper" if self.upper else "None", "tail" if self.tail else "None")

class MyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def getNode(self, index: int) -> Node:
        if index >= 0 and index < self.length:
            node = self.first
            for _ in range(index):
                node = node.tail
            return node
        else:
            return None

    def get(self, index: int) -> int:
        return -1 if index >= len(self) else self.getNode(index).value

    def addAtHead(self, val: int) -> None:
        if self.first:
            oldNode = self.first
            newNode = Node(val, None, oldNode)
            oldNode.upper = newNode
            self.first = newNode
        else:
            self.first = Node(val, None, None)
            self.last = self.first
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.last:
            oldNode = self.last
            newNode = Node(val, oldNode, None)
            oldNode.tail = newNode
            self.last = newNode
        else:
            self.last = Node(val, None, None)
            self.first = self.last
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index == len(self):
            self.addAtTail(val)
            return
        if index < len(self) and index >= 0:
            node = self.getNode(index)

            oldUpper = node.upper
            oldTail = node
            newNode = Node(val, oldUpper, oldTail)
            oldUpper.tail = newNode
            oldTail.upper = newNode
            self.length += 1

    def deleteFromHead(self):
        if len(self):
            if self.first == self.last:
                self.first = None
                self.last = None
            elif self.first:
                newFirst = self.first.tail
                newFirst.upper = None
                self.first = newFirst
            self.length -= 1

    def deleteFromLast(self):
        if len(self):
            if self.first == self.last:
                self.first = None
                self.last = None
            elif self.last:
                newLast = self.last.upper
                newLast.tail = None
                self.last = newLast
            self.length -= 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.deleteFromHead()
            return
        if index == len(self)-1:
            self.deleteFromLast()
            return

        if index >= 0 and index < self.length:
            node = self.getNode(index)
            newUpper = node.upper
            newTail = node.tail
            newUpper.tail = newTail
            newTail.upper = newUpper
            self.length -= 1

    def __str__(self) -> str:
        res = "MyLinkedList("
        currentList = self.first
        while currentList:
            res += str(currentList.value)
            if currentList.tail:
                res += ","
            currentList = currentList.tail
        res += ")"
        return res

    def __len__(self):
        return self.length
