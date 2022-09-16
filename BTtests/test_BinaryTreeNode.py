import pytest
from collections import namedtuple

from BinaryTreeNode import BinaryTreeNode
from BinaryTree import BinaryTree

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



def test_init_node(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node = BinaryTreeNode(person1)
    assert node.value == person1
    assert node.left is None
    assert node.right is None

def test_str(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node = BinaryTreeNode(person1)
    assert str(node) == "Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224', Poststed='MELHUS')"

def test_node_hasRight(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node = BinaryTreeNode(person1)
    node.right = BinaryTreeNode(person2)
    assert node.right.value == person2
    assert node.right.right is None


def test_node_hasLeft(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node = BinaryTreeNode(person1)
    node.left = BinaryTreeNode(person2)
    assert node.left.value == person2
    assert node.left.left is None


def test_prefixOrder_full_tree(test_tree_full, capfd):
    test_tree_full._root.prefixOrder()
    out, err = capfd.readouterr()
    assert out == "Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224', Poststed='MELHUS')  \nPerson(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361', Poststed='ØSTERÅS')  \nPerson(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948', Poststed='FEDJE')  \n"

def test_prefixOrder_empty_tree(capfd):
    test_tree_empty = BinaryTree()
    test_tree_empty._root.prefixOrder()
    #out, err = capfd.readouterr()
    #assert out == ""

def test_infixOrder_full_tree(test_tree_full, capfd):
    test_tree_full._root.infixOrder()
    out, err = capfd.readouterr()
    assert out == "Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361', Poststed='ØSTERÅS')  \nPerson(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224', Poststed='MELHUS')  \nPerson(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948', Poststed='FEDJE')  \n"

def test_infixOrder_empty_tree(capfd):
    test_tree_empty = BinaryTree()
    test_tree_empty._root.infixOrder()
    #out, err = capfd.readouterr()
    #assert out == ""

def test_postfixOrder_full_tree(test_tree_full, capfd):
    test_tree_full._root.postfixOrder()
    out, err = capfd.readouterr()
    assert out == "Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361', Poststed='ØSTERÅS')  \nPerson(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948', Poststed='FEDJE')  \nPerson(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224', Poststed='MELHUS')  \n"

def test_postfixOrder_empty_tree(capfd):
    test_tree_empty = BinaryTree()
    test_tree_empty._root.postfixOrder()
    #out, err = capfd.readouterr()
    #assert out == ""

def test_levelOrder_full_tree(test_tree_full, capfd):
    test_tree_full._root.levelOrder()
    out, err = capfd.readouterr()
    assert out == "Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224', Poststed='MELHUS')  \nPerson(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361', Poststed='ØSTERÅS')  \nPerson(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948', Poststed='FEDJE')  \n"

def test_levelOrder_empty_tree(capfd):
    test_tree_empty = BinaryTree()
    test_tree_empty._root.levelOrder()
    #out, err = capfd.readouterr()
    #assert out == ""

def test_equality(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node2 = BinaryTreeNode(person1)
    node3 = BinaryTreeNode(person2)
    node4 = BinaryTreeNode(None)
    assert node1 == node2
    assert node1.value == node2.value
    assert not node1 == node3
    assert node4 == None


def test_notequal_1(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node2 = BinaryTreeNode(person2)
    assert node1 != node2

def test_notequal_2(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node2 = BinaryTreeNode(person1)
    assert not node1 != node2

def test_notequal_3(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node4 = BinaryTreeNode(None)
    assert node4 != node1


def test_lower_than(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node2 = BinaryTreeNode(person2)
    node3 = BinaryTreeNode(person3)
    node4 = BinaryTreeNode(None)
    assert node2 < node1
    assert node2.value < node1.value
    assert not node3 < node2
    assert not node4 < node1

def test_lower_than_2(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node4 = BinaryTreeNode(None)
    assert node4 < node1

def test_lower_than_3():
    node4 = BinaryTreeNode(None)
    assert not node4 < None

def test_lower_than_4(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    assert not node1 < None

def test_lower_than_or_equal(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node2 = BinaryTreeNode(person2)
    node3 = BinaryTreeNode(person3)
    assert node2 <= node1
    assert node2.value <= node1.value
    assert not node3 <= node2
    assert node3 <= node3

def test_lower_than_or_equal_2(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node4 = BinaryTreeNode(None)
    assert node4 <= node1

def test_lower_than_or_equal_3():
    node4 = BinaryTreeNode(None)
    assert node4 <= None


def test_greater_than(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node2 = BinaryTreeNode(person2)
    node3 = BinaryTreeNode(person3)
    assert node1 > node2
    assert node1.value > node2.value
    assert not node2 > node3

def test_greater_than_2(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node4 = BinaryTreeNode(None)
    assert node1 > node4

def test_greater_than_3(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    assert node1 > None

def test_greater_than_4():
    node4 = BinaryTreeNode(None)
    assert not node4 > None


def test_greater_than_or_equal(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node2 = BinaryTreeNode(person2)
    node3 = BinaryTreeNode(person3)
    assert node1 >= node2
    assert node1.value >= node2.value
    assert not node2 >= node3
    assert node3 >= node3

def test_greater_than_or_equal_2(sample_persons):
    person1, person2, person3, person4 = sample_persons
    node1 = BinaryTreeNode(person1)
    node4 = BinaryTreeNode(None)
    assert node1 >= node4

def test_greater_than_or_equal_3():
    node4 = BinaryTreeNode(None)
    assert node4 >= None
