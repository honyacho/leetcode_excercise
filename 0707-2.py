class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = None
        self.last = None


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if len(self) <= index:
            return -1
        currentIndex = 0
        result = None
        currentList = self.first
        while currentList and currentIndex <= index:
            result = currentList.value
            currentIndex += 1
            currentList = currentList.tail
        return result
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.first:
            oldNode = self.first
            newNode = Node(val, None, oldNode)
            oldNode.upper = newNode
            self.first = newNode
        else:
            self.first = Node(val, None, None)
            self.last = self.first

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.last:
            oldNode = self.last
            newNode = Node(val, oldNode, None)
            oldNode.tail = newNode
            self.last = newNode
        else:
            self.last = Node(val, None, None)
            self.first = self.last

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        currentIndex = 0
        currentList = self.first
        oldUpper = currentList and currentList.upper
        oldTail = currentList and currentList.tail

        while currentList and currentIndex < index:
            currentIndex += 1
            currentList = currentList.tail

        # here you have the element at index
        if currentList:
            oldUpper = currentList.upper
            oldTail = currentList # .tail
            newNode = Node(val, oldUpper, oldTail)
            if oldUpper:
                oldUpper.tail = newNode
            if oldTail:
                oldTail.upper = newNode
            if not newNode.tail:
                self.last = newNode
            if not newNode.upper:
                self.first = newNode

        else:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            if self.first == self.last:
                self.first = None
                self.last = None
            elif self.first:
                newFirst = self.first.tail
                newFirst.upper = None
                self.first = newFirst
            return

        currentIndex = 0
        currentList = self.first

        while currentList and currentIndex < index:
            currentIndex += 1
            currentList = currentList.tail

        # 終端の場合
        if currentList == self.last:
            newLast = currentList.upper
            newLast.tail = None
            self.last = newLast
        # 真ん中の場合
        else:
            if currentList:
                newUpper = currentList.upper
                newTail = currentList.tail
                newUpper.tail = newTail
                if newTail:
                    newTail.upper = newUpper

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
        size = 0
        currentList = self.first
        while currentList:
            size += 1
            currentList = currentList.tail
        return size

class Node:
    def __init__(self, value, upper, tail):
        self.value = value
        self.tail = tail
        self.upper = upper
    
    def __str__(self):
        return "Node({},{},{})".format(self.value, "upper" if self.upper else "None", "tail" if self.tail else "None")