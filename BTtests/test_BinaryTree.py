# Tests marked with @pytest.mark.xfail are throwing exceptions before assert is reached.
# From docs.pytest.org:
# Using pytest.raises() is likely to be better for cases where you are testing exceptions your own code is
# deliberately raising, whereas using @pytest.mark.xfail with a check function is probably better for something
# like documenting unfixed bugs.
# I did not want to write "with not pytest.raises(Exception):" for every test I knew would fail with an exception,
# so I used @pytest.mark.xfail.
# Please use "pytest -v -m xfail" to see which tests are failing due to exceptions.

import pytest
from collections import namedtuple

from BinaryTree import BinaryTree
from BinaryTreeNode import BinaryTreeNode

Person = namedtuple('Person', ["Etternavn", "Fornavn", "Adresse", "Postnummer", "Poststed"])


############# FIXTURES #############

@pytest.fixture()
def sample_persons():  # 8 persons so we do not have to rely on Personer.dta. Its presence is not a given.
    person1 = Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224',
                     Poststed='MELHUS')
    person2 = Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361',
                     Poststed='ØSTERÅS')
    person3 = Person(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948',
                     Poststed='FEDJE')
    person4 = Person(Etternavn='NOTFOUND', Fornavn='NOTFOUND', Adresse='NOTFOUND', Postnummer='NOTFOUND',
                     Poststed='NOTFOUND')
    person5 = Person(Etternavn='B', Fornavn='B', Adresse='B', Postnummer='B', Poststed='B')
    person6 = Person(Etternavn='Z', Fornavn='Z', Adresse='Z', Postnummer='Z', Poststed='Z')
    person7 = Person(Etternavn='H', Fornavn='H', Adresse='H', Postnummer='H', Poststed='H')
    person8 = Person(Etternavn='A', Fornavn='A', Adresse='A', Postnummer='A', Poststed='A')

    return person1, person2, person3, person4, person5, person6, person7, person8


@pytest.fixture()
def test_tree_full():
    test_list = [Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224',
                        Poststed='MELHUS'),
                 Person(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948',
                        Poststed='FEDJE'),
                 Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361',
                        Poststed='ØSTERÅS')]
    test_tree_full = BinaryTree()
    for i in range(3):
        test_tree_full.insert(value=test_list[i])
    return test_tree_full


############# TESTS #############


def test_init_tree(sample_persons):
    tree = BinaryTree()
    assert tree._root is None
    node1 = BinaryTreeNode(sample_persons[0])
    tree = BinaryTree(node1)
    assert tree._root == node1
    tree2 = BinaryTree("NOT A NODE")
    assert tree2._root is None


def test_findLeftMost(test_tree_full, sample_persons):
    assert test_tree_full.findLeftMost(test_tree_full._root) == test_tree_full._root.left
    test_tree_full.insert(value=sample_persons[4])
    assert test_tree_full.findLeftMost(test_tree_full._root) == test_tree_full._root.left.left


def test_findRightMost(test_tree_full, sample_persons):
    assert test_tree_full.findRightMost(test_tree_full._root) == test_tree_full._root.right
    test_tree_full.insert(value=sample_persons[5])
    assert test_tree_full.findRightMost(test_tree_full._root) == test_tree_full._root.right.right


def test_findMin(test_tree_full):
    assert test_tree_full.findMin() == test_tree_full._root.left


def test_findMin_2(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[4])
    assert test_tree_full.findMin() == test_tree_full._root.left.left


def test_findMax(test_tree_full, sample_persons):
    assert test_tree_full.findMax() == test_tree_full._root.right


def test_findMax_2(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[5])
    assert test_tree_full.findMax() == test_tree_full._root.right.right


# Line 41 in the find function cannot be reached as far as I can see. If it's not ">", "<" or "==", the only other
# option is that value = None which causes a TypeError and breaks the program before reaching the else: statement.

def test_find(test_tree_full, sample_persons):
    assert test_tree_full.find(sample_persons[0]) == test_tree_full._root
    assert test_tree_full.find(sample_persons[1]) == test_tree_full._root.left
    assert test_tree_full.find(sample_persons[2]) == test_tree_full._root.right
    test_tree_full.insert(value=sample_persons[4])
    assert test_tree_full.find(sample_persons[4]) == test_tree_full._root.left.left


def test_find_in_empty_tree(sample_persons):
    tree = BinaryTree()
    assert tree.find(key=sample_persons[0]) is None
    assert tree.find(key=sample_persons[1]) is None


def test_find_not_found(test_tree_full, sample_persons):
    assert test_tree_full.find(key=sample_persons[3]) is None


# If no key is entered the function should return the root node, or at least not break with a TypeError
# Marked with xfail
@pytest.mark.xfail(raises=TypeError)
def test_find_key_none(test_tree_full):
    assert test_tree_full.find(key=None) is test_tree_full._root


def test_insert(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[3])
    test_tree_full.insert(value=sample_persons[4])
    assert test_tree_full.find(key=sample_persons[3]) == test_tree_full._root.right.left
    assert test_tree_full.find(key=sample_persons[4]) == test_tree_full._root.left.left


def test_insert_into_empty(sample_persons):
    test_tree = BinaryTree()
    node1 = BinaryTreeNode(sample_persons[0])
    test_tree.insert(treenode=node1)
    assert test_tree._root == node1
    test_tree = BinaryTree()
    test_tree.insert(value=sample_persons[0])
    assert test_tree._root.value == sample_persons[0]


def test_insert_already_exists(test_tree_full, sample_persons):
    with pytest.raises(Exception):
        test_tree_full.insert(value=sample_persons[0])


def test_insert_none():
    tree = BinaryTree()
    with pytest.raises(Exception):
        tree.insert(value=None)


def test_insert_none_2():
    tree = BinaryTree()
    with pytest.raises(Exception):
        tree.insert(treenode=None)


def test_insert_none_3():
    tree = BinaryTree()
    node = BinaryTreeNode(value=None)
    with pytest.raises(Exception):
        tree.insert(treenode=node)


# In order to reach lines 81-83 I had to write a specific test where current and treenode are identical and value is
# None and try to insert them into an empty tree. It seems odd to cover a case referencing a non-existent node in an
# empty tree and trying to insert its duplicate.

def test_insert_with_current_and_treenode(sample_persons):
    node1 = BinaryTreeNode(sample_persons[0])
    node2 = BinaryTree(sample_persons[1])
    tree = BinaryTree()
    tree.insert(current=node1, treenode=node1)
    assert tree._root == node1


# The way equality is set up in BinaryTreeNode, the check treenode == None is true if treenode.value is None.
# Therefor line 51 is unreachable and obsolete.

# Only testing _getnodes exception. _getnodes is called by insert and insert has been tested.
def test_getnodes(sample_persons):
    node1 = BinaryTreeNode(sample_persons[0])
    node2 = BinaryTreeNode(sample_persons[1])
    test_tree = BinaryTree()
    test_tree.insert(value=node1)
    with pytest.raises(Exception):
        test_tree._getnodes(None, None, None)
    with pytest.raises(Exception):
        test_tree._getnodes(None, node1, node2)


def test_deleteMin(test_tree_full):
    test_tree_full.deleteMin()
    assert test_tree_full.findMin() == test_tree_full._root


def test_deleteMin_2(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[4])
    test_tree_full.deleteMin()
    assert test_tree_full.findMin() == test_tree_full._root.left


def test_deleteMin_3(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[6])
    test_tree_full.deleteMin()
    assert test_tree_full.findMin() == test_tree_full._root.left


# If the tree is empty, deleteMin should return None or a message that the tree is empty.
@pytest.mark.xfail(raises=AttributeError)
def test_deleteMin_empty_tree():
    test_tree = BinaryTree()
    test_tree.deleteMin()
    # assert test_tree._root is None


def test_deleteMin_one_node(sample_persons):
    test_tree = BinaryTree()
    test_tree.insert(value=sample_persons[0])
    test_tree.deleteMin()
    assert test_tree._root is None


def test_deleteMin_two_nodes(sample_persons):
    test_tree = BinaryTree()
    test_tree.insert(value=sample_persons[0])
    test_tree.insert(value=sample_persons[2])
    test_tree.deleteMin()
    assert test_tree._root.value == sample_persons[2]


def test_deleteMax(test_tree_full):
    test_tree_full.deleteMax()
    assert test_tree_full.findMax() == test_tree_full._root


def test_deleteMax_2(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[3])
    test_tree_full.deleteMax()
    assert test_tree_full.findMax() == test_tree_full._root.right


def test_deleteMax_3(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[5])
    test_tree_full.deleteMax()
    assert test_tree_full.findMax() == test_tree_full._root.right


# If the tree is empty, deleteMax should return None or a message that the tree is empty.
@pytest.mark.xfail(raises=AttributeError)
def test_deleteMax_empty_tree():
    test_tree = BinaryTree()
    test_tree.deleteMax()
    # assert test_tree._root is None


# DeleteMax is a copy of deleteMin when it comes to functionality, however it is missing some code which leads to it
# breaking with an AttributeError if root has no right node.

@pytest.mark.xfail(raises=AttributeError)
def test_deleteMax_one_node(sample_persons):
    test_tree = BinaryTree()
    test_tree.insert(value=sample_persons[0])
    test_tree.deleteMax()
    # assert test_tree._root is None


@pytest.mark.xfail(raises=AttributeError)
def test_deleteMax_two_nodes(sample_persons):
    test_tree = BinaryTree()
    test_tree.insert(value=sample_persons[0])
    test_tree.insert(value=sample_persons[1])
    test_tree.deleteMax()
    # assert test_tree._root.value == sample_persons[1]


def test_delete_and_reorder(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[3])
    assert test_tree_full.find(key=sample_persons[3]) == test_tree_full._root.right.left
    test_tree_full.delete(key=sample_persons[0])
    assert test_tree_full.find(key=sample_persons[0]) is None
    assert test_tree_full.find(key=sample_persons[3]) == test_tree_full._root


def test_delete_and_reorder_2(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[3])
    test_tree_full.insert(value=sample_persons[4])
    test_tree_full.insert(value=sample_persons[5])
    test_tree_full.insert(value=sample_persons[6])
    test_tree_full.delete(key=sample_persons[5])
    assert test_tree_full.find(key=sample_persons[5]) is None
    assert test_tree_full.find(key=sample_persons[6]) == test_tree_full._root.left.right


def test_delete_and_reorder_3(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[3])
    test_tree_full.insert(value=sample_persons[4])
    test_tree_full.insert(value=sample_persons[5])
    test_tree_full.insert(value=sample_persons[6])
    test_tree_full.delete(key=sample_persons[2])
    assert test_tree_full.find(key=sample_persons[2]) is None
    assert test_tree_full.find(key=sample_persons[3]) == test_tree_full._root.right.left


def test_delete_and_reorder_4(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[3])
    test_tree_full.insert(value=sample_persons[4])
    test_tree_full.insert(value=sample_persons[5])
    test_tree_full.insert(value=sample_persons[6])
    test_tree_full.insert(value=sample_persons[7])
    test_tree_full.delete(key=sample_persons[4])
    assert test_tree_full.find(key=sample_persons[4]) is None
    assert test_tree_full.find(key=sample_persons[1]) == test_tree_full._root.left

def test_delete_root(sample_persons):
    test_tree = BinaryTree()
    test_tree.insert(value=sample_persons[0])
    test_tree.delete(key=sample_persons[0])
    assert test_tree._root is None


def test_delete_left(test_tree_full, sample_persons):
    test_tree_full.delete(key=sample_persons[1])
    assert test_tree_full.find(key=sample_persons[1]) is None
    assert test_tree_full._root.left is None


def test_delete_right(test_tree_full, sample_persons):
    test_tree_full.insert(value=sample_persons[3])
    test_tree_full.delete(key=sample_persons[2])
    assert test_tree_full.find(key=sample_persons[2]) is None
    assert test_tree_full._root.right.value == sample_persons[3]


# Trying to delete a node that does not exist in the tree should return a message that the node does not exist.
# Trying to delete a node when the tree is empty should return a message that the tree is empty.
# Trying to use the delete command without giving a key should return a message that a key is required.
@pytest.mark.xfail(raises=AttributeError)
def test_delete_not_found(test_tree_full, sample_persons):
    test_tree_full.delete(key=sample_persons[3])


@pytest.mark.xfail(raises=AttributeError)
def test_delete_empty_tree(sample_persons):
    test_tree = BinaryTree()
    test_tree.delete(key=sample_persons[0])
    # assert test_tree._root is None


# Found no way to access line 141. Key has to be comparable via "<" and ">" as well as "==". There is no else.
@pytest.mark.xfail(raises=AttributeError)
def test_delete_none():
    test_tree = BinaryTree()
    test_tree.delete(key=None)
    # assert test_tree._root is None


