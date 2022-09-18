from io import StringIO
import sys


class MyBinaryNode:
    def __init__(self, value, left_tree=None, right_tree=None):
        self.value = value
        self.left = left_tree
        self.right = right_tree

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left_tree):
        self.__left = left_tree

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right_tree):
        self.__right = right_tree

    def __eq__(self, node):
        if node is None:
            return False
        elif not isinstance(node, MyBinaryNode):
            raise Exception("Can only compare MyBinaryNode to MyBinaryNode")
        else:
            return self.value == node.value and self.left == node.left and self.right == node.right

    def __str__(self):
        return str(self.value)

    def has_right(self):
        return self.right is not None

    def has_left(self):
        return self.left is not None

    def info(self):
        retval = self.value + " : ( "
        if isinstance(self.left, MyBinaryNode):
            retval += self.left.value
        else:
            retval += "None"
        retval += " , "
        if isinstance(self.right, MyBinaryNode):
            retval += self.right.value + " )"
        else:
            retval += "None )"
        return retval

    def prefixOrder(self):
        print(self, ' ', end='')
        if self.has_left():
            self.left.prefixOrder()
        if self.has_right():
            self.right.prefixOrder()

    def infixOrder(self):
        if self.has_left():
            self.left.infixOrder()
        print(self, ' ', end='')
        if self.has_right():
            self.right.infixOrder()

    def postfixOrder(self):
        if self.has_left():
            self.left.postfixOrder()
        if self.has_right():
            self.right.postfixOrder()
        print(self, ' ', end='')


def calculate(result):
    try:
        print(eval(result))
    except:
        return


def main():
    oper_list = input("Enter a list of operators and operands: ").split()
    left_node = MyBinaryNode(oper_list[1], MyBinaryNode(oper_list[2]), MyBinaryNode(oper_list[3]))
    right_node = MyBinaryNode(oper_list[4], MyBinaryNode(oper_list[5]), MyBinaryNode(oper_list[6]))
    root_node = MyBinaryNode(oper_list[0], left_node, right_node)
    s = StringIO()
    print(f"\nInfix order: {root_node.infixOrder()}", end='')
    print(f"\nInfix order: {root_node.infixOrder()}", end='', file=s)
    result = s.getvalue()
    calculate(result)
    print(f"\nPostfix order: {root_node.postfixOrder()}", end='')
    print(f"\nPostfix order: {root_node.postfixOrder()}", end='', file=s)
    result = s.getvalue()
    calculate(result)


if __name__ == '__main__':
    main()
