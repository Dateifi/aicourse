class MyNode:
    def __init__(self, data=None):
        self.previous = None
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# double linked list

class MyLinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
            self.tail = None
        elif type(data) == list:
            self.head = None
            self.tail = None
            for i in data:
                self.append(i)
        else:
            self.head = MyNode(data)
            self.tail = self.head
            self.head.previous = None
            self.tail.next = None

    def __getitem__(self, idx):
        current = self.head
        try:
            for i in range(idx):
                current = current.next
            return current.data
        except AttributeError:
            raise IndexError


    def __setitem__(self, idx, item):
        current = self.head
        try:
            for i in range(idx):
                current = current.next
            current.data = item
        except AttributeError:
            raise IndexError


    def __add__(self, list2):
        new_list = MyLinkedList()
        for i in self:
            new_list.append(i)
        for i in list2:
            new_list.append(i)
        return new_list


    def append(self, data):

        new_node = MyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.tail.next = None


    def insert(self, idx, item):
        new_node = MyNode(item)
        current = self.head
        for i in range(idx):
            current = current.next
        if current.previous is not None:
            current.previous.next = new_node
            new_node.previous = current.previous
        else:
            self.head = new_node
        current.previous = new_node
        new_node.next = current

    def __delitem__(self, idx):
        current = self.head
        for i in range(idx):
            current = current.next
        if current.previous is not None:
            current.previous.next = current.next
        else:
            self.head = current.next
        if current.next is not None:
            current.next.previous = current.previous
        else:
            self.tail = current.previous

    def __eq__(self, list2):
        if len(self) != len(list2):
            return False
        for i in range(len(self)):
            if self[i] != list2[i]:
                return False
        return True

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __len__(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def __contains__(self, item):
        for i in self:
            if i == item:
                return True
        return False

    def __str__(self):
        string = "[ "
        current = self.head
        while current is not None:
            string += str(current.data) + " "
            current = current.next
        return string + "]"


class MyStack(MyLinkedList):
    def __init__(self):
        super().__init__()

    def push(self, data):
        self.append(data)

    def top(self):
        return self.tail.data

    def peek(self):
        return self[len(self) - 1]

    def pop(self):
        try:
            data = self[len(self) - 1]
            del self[len(self) - 1]
            return data
        except IndexError:
            raise IndexError


class MyFIFO(MyLinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        try:
            data = self[0]
            del self[0]
            return data
        except IndexError:
            raise IndexError



