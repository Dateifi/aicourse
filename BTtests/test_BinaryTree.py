import pytest
from collections import namedtuple

from BinaryTree import BinaryTree
from BinaryTreeNode import BinaryTreeNode

Person = namedtuple('Person', ["Etternavn", "Fornavn", "Adresse", "Postnummer", "Poststed"])


@pytest.fixture
def sample_persons():
    person1 = Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224',
                     Poststed='MELHUS')
    person2 = Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361',
                     Poststed='ØSTERÅS')
    person3 = Person(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948',
                     Poststed='FEDJE')
    person4 = Person(Etternavn='NOTFOUND', Fornavn='NOTFOUND', Adresse='NOTFOUND', Postnummer='NOTFOUND',
                     Poststed='NOTFOUND')

    return person1, person2, person3, person4


@pytest.fixture
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


def test_init_tree(sample_persons):
    person1, person2, person3, person4 = sample_persons
    tree = BinaryTree()
    assert tree._root is None
    node1 = BinaryTreeNode(person1)
    tree = BinaryTree(node1)
    assert tree._root == node1


def test_findLeftMost(test_tree_full):
    assert test_tree_full.findLeftMost(test_tree_full._root) == test_tree_full._root.left


def test_findRightMost(test_tree_full):
    assert test_tree_full.findRightMost(test_tree_full._root) == test_tree_full._root.right


def test_findMin(test_tree_full):
    assert test_tree_full.findMin() == test_tree_full._root.left


def test_findMax(test_tree_full):
    assert test_tree_full.findMax() == test_tree_full._root.right


def test_find(test_tree_full):
    assert test_tree_full.find(
        Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224',
               Poststed='MELHUS')) == test_tree_full._root
    assert test_tree_full.find(
        Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361',
               Poststed='ØSTERÅS')) == test_tree_full._root.left
    assert test_tree_full.find(Person(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948',
                                      Poststed='FEDJE')) == test_tree_full._root.right


def test_getnodes(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node2 = BinaryTreeNode(person2)
    test_tree = BinaryTree()
    test_tree.insert(value=node1)
    with pytest.raises(Exception):
        test_tree._getnodes(None, None, None)
    with pytest.raises(Exception):
        test_tree._getnodes(None, node1, node2)


def test_find_in_empty_tree(sample_persons):
    person1, person2, person3, person4 = sample_persons
    tree = BinaryTree()
    assert tree.find(key=person1) is None


def test_find_not_found(test_tree_full, sample_persons):
    person1, person2, person3, person4 = sample_persons
    assert test_tree_full.find(key=person4) is None
    # with pytest.raises(KeyError):  Found no way to reach the KeyError in the find function
    #    test_tree_full.find("NOTFOUND")


def test_insert(test_tree_full, sample_persons):
    person1, person2, person3, person4 = sample_persons
    person5 = Person(Etternavn='Ø', Fornavn='Ø', Adresse='Ø', Postnummer='Ø', Poststed='Ø')
    test_tree_full.insert(value=person4)
    test_tree_full.insert(value=person5)
    assert test_tree_full.find(key=person4) == test_tree_full._root.right.left
    assert test_tree_full.find(key=person5) == test_tree_full._root.right.right


def test_insert_into_empty(sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree = BinaryTree()
    node1 = BinaryTreeNode(person1)
    test_tree.insert(treenode=node1)
    assert test_tree._root == node1


def test_insert_already_exists(test_tree_full, sample_persons):
    person1, person2, person3, person4 = sample_persons
    with pytest.raises(Exception):
        test_tree_full.insert(value=person1)


def test_insert_empty_tree(sample_persons):
    person1, person2, person3, person4 = sample_persons
    tree = BinaryTree()
    tree.insert(value=person1)
    assert tree._root.value == person1


def test_insert_none():
    tree = BinaryTree()
    with pytest.raises(Exception):
        tree.insert(value=None)


def test_deleteMin(test_tree_full):
    test_tree_full.deleteMin()
    assert test_tree_full.findMin() == test_tree_full._root


def test_deleteMax(test_tree_full):
    test_tree_full.deleteMax()
    assert test_tree_full.findMax() == test_tree_full._root


def test_delete(test_tree_full, sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree_full.insert(value=person4)
    assert test_tree_full.find(key=person4) == test_tree_full._root.right.left
    test_tree_full.delete(key=person1)
    assert test_tree_full.find(key=person1) is None
    assert test_tree_full.find(key=person4) == test_tree_full._root


def test_delete_2(test_tree_full, sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree_full.delete(key=person2)
    assert test_tree_full.find(key=person2) is None
    assert test_tree_full._root.left is None


def test_delete_3(test_tree_full, sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree_full.insert(value=person4)
    test_tree_full.delete(key=person3)
    assert test_tree_full.find(key=person3) is None
    assert test_tree_full._root.right.value == person4


def test_delete_not_found(test_tree_full, sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree_full.delete(key=person4)


def test_delete_empty_tree(sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree = BinaryTree()
    test_tree.delete(key=person1)
    assert test_tree._root is None


def test_delete_none():
    test_tree = BinaryTree()
    test_tree.delete(key=None)
    assert test_tree._root is None


def test_deleteMin_empty_tree():
    test_tree = BinaryTree()
    test_tree.deleteMin()
    assert test_tree._root is None


def test_deleteMax_empty_tree():
    test_tree = BinaryTree()
    test_tree.deleteMax()
    assert test_tree._root is None


def test_deleteMin_one_node(sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree = BinaryTree()
    test_tree.insert(value=person1)
    test_tree.deleteMin()
    assert test_tree._root is None


def test_deleteMax_one_node(sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree = BinaryTree()
    test_tree.insert(value=person1)
    test_tree.deleteMax()
    assert test_tree._root is None


def test_deleteMin_two_nodes(sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree = BinaryTree()
    test_tree.insert(value=person1)
    test_tree.insert(value=person2)
    test_tree.deleteMin()
    assert test_tree._root.value == person1


def test_deleteMax_two_nodes(sample_persons):
    person1, person2, person3, person4 = sample_persons
    test_tree = BinaryTree()
    test_tree.insert(value=person1)
    test_tree.insert(value=person2)
    test_tree.deleteMax()
    assert test_tree._root.value == person2
