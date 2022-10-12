import warnings

from binarytree import Node


class BinarySearchTree:
    # Initialize the tree
    def __init__(self, root=None):
        self.root = root
        # Check if root is a valid Node
        if isinstance(self.root, Node):
            if not self.validate_node(self.root):
                raise ValueError("Node has invalids branches/leafs for a search tree")
        elif self.root is not None:
            raise ValueError("Root must be a Node or None")

    # Insert a new node into the tree
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value == current.value:
                warnings.warn("Value already exists in tree")
                return
            elif value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    # Find a node in the tree
    def find(self, value=None):
        if value is None:
            warnings.warn("No value given or value is None")
            return None

        level = 0
        current = self.root
        while current is not None:
            if value == current.value:
                return current, level
            elif value < current.value:
                current = current.left
                level += 1
            else:
                current = current.right
                level += 1
        raise KeyError("Value not found in tree")

    # Helper function to find inorder successor for delete function
    def find_min(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    # Delete a node from the tree
    def delete(self, value=None):
        if value is None:
            warnings.warn("No value given or value is None")
            return
        if self.root is None:
            raise KeyError("Cannot delete from empty tree")

        # Save and update parent and current references
        parent = None
        current = self.root

        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            raise KeyError("Value not found in tree")

        # Node is a leaf node (no children), if it is the root node, set root to None, otherwise set
        # parent.left/right reference to None
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # Node has 2 children, find the inorder successor and replace the current node with it
        elif current.left and current.right:
            successor = self.find_min(current.right)
            succ_value = successor.value
            self.delete(successor.value)
            current.value = succ_value

        # Node has one child, if it is the root node, set root to the child, otherwise set parent.left/right
        # reference to the child
        else:
            if current.left:
                child = current.left
            else:
                child = current.right

            if parent is None:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

    def validate_node(self, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            if node.left.value > node.value:
                return False
            if not self.validate_node(node.left):
                return False

        if node.right is not None:
            if node.right.value < node.value:
                return False
            if not self.validate_node(node.right):
                return False

        return True

    def level(self, node):
        if node is None and self.root is None:
            warnings.warn("No node given and tree is empty")
            return 0
        elif node is None:
            warnings.warn("No value specified, using root node")
            return 0

        else:
            return node.find(node.value)[1]


def main():
    t = BinarySearchTree()
    t.insert(7)
    t.insert(4)
    t.insert(13)
    t.insert(2)
    t.insert(6)
    t.insert(9)
    t.insert(15)
    t.insert(5)
    t.insert(1)
    t.insert(8)
    t.insert(11)
    t.insert(12)


