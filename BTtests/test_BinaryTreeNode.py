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

from BinaryTreeNode import BinaryTreeNode
from BinaryTree import BinaryTree




############# FIXTURES #############

@pytest.fixture(scope="module")
def sample_persons():  # 4 persons so we do not have to rely on Personer.dta. Its presence is not a given.
    Person = namedtuple('Person', ["Etternavn", "Fornavn", "Adresse", "Postnummer", "Poststed"])
    person1 = Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', Postnummer='7224',
                     Poststed='MELHUS')
    person2 = Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361',
                     Poststed='ØSTERÅS')
    person3 = Person(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948',
                     Poststed='FEDJE')
    person4 = Person(Etternavn='NOTFOUND', Fornavn='NOTFOUND', Adresse='NOTFOUND', Postnummer='NOTFOUND',
                     Poststed='NOTFOUND')

    return person1, person2, person3, person4


@pytest.fixture(scope="module")
def sample_nodes(sample_persons):  # 4 nodes as well as an empty node to use for testing
    node1 = BinaryTreeNode(sample_persons[0])
    node2 = BinaryTreeNode(sample_persons[1])
    node3 = BinaryTreeNode(sample_persons[2])
    node4 = BinaryTreeNode(sample_persons[3])
    node5 = BinaryTreeNode(None)

    return node1, node2, node3, node4, node5


@pytest.fixture(scope="module")
def linked_nodes(sample_nodes):  # 3 linked nodes to test order functions
    root_node = sample_nodes[0]
    root_node.left = sample_nodes[1]
    root_node.right = sample_nodes[2]

    return root_node


############# TESTS #############

def test_init_node(sample_persons):
    test_node = BinaryTreeNode(sample_persons[0])
    assert test_node.value == sample_persons[0]
    assert test_node.left is None
    assert test_node.right is None


def test_init_node_with_links(sample_nodes):
    test_node = BinaryTreeNode(sample_nodes[0], sample_nodes[1], sample_nodes[2])
    assert test_node.value == sample_nodes[0]
    assert test_node.left == sample_nodes[1]
    assert test_node.right == sample_nodes[2]


# Testing BinaryTreeNode on its own merits, there is nothing wrong creating nodes with value None. However,
# the BinaryTree class does not allow the insertion of nodes with value None. Furthermore, the equality and
# comparison tests in this class cause issues with certain functions in the BinaryTree class. See below.
def test_init_node_none():
    test_node = BinaryTreeNode(None)
    assert test_node.value is None
    assert test_node.left is None
    assert test_node.right is None


def test_init_node_none_with_links(sample_nodes):
    test_node = BinaryTreeNode(None, sample_nodes[1], sample_nodes[2])
    assert test_node.value is None
    assert test_node.left == sample_nodes[1]
    assert test_node.right == sample_nodes[2]


# This test fails because the __str__ function simply returns the NamedTuple. Which is not allowed. A __str__
# function always has to return a string. Replacing "return self.value" with actual string formatting would fix this.
# The most likely reason for this error is that the author of this tree made it for a use case that did not include
# NamedTuples.

@pytest.mark.xfail(raises=TypeError)
def test_str(sample_persons):
    test_node = BinaryTreeNode(sample_persons[0])
    assert isinstance(str(test_node), str)


def test_node_hasRight(linked_nodes):
    root_node = linked_nodes
    assert root_node.hasRight() is True
    assert root_node.right.hasRight() is False


def test_node_hasLeft(linked_nodes):
    root_node = linked_nodes
    assert root_node.hasLeft() is True
    assert root_node.left.hasLeft() is False


def test_prefixOrder_linked_nodes(linked_nodes, capfd):
    root_node = linked_nodes
    root_node.prefixOrder()
    out, err = capfd.readouterr()
    assert out == "Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', " \
                  "Postnummer='7224', Poststed='MELHUS')  \nPerson(Etternavn='GJERSTAD', Fornavn='TORKJELL', " \
                  "Adresse='HOSTELAND 2 83', Postnummer='1361', Poststed='ØSTERÅS')  \nPerson(Etternavn='OLDERVIK', " \
                  "Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948', Poststed='FEDJE')  \n"


def test_infixOrder_linked_nodes(linked_nodes, capfd):
    root_node = linked_nodes
    root_node.infixOrder()
    out, err = capfd.readouterr()
    assert out == "Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361', " \
                  "Poststed='ØSTERÅS')  \nPerson(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', " \
                  "Adresse='LEINAHYTTA 36', Postnummer='7224', Poststed='MELHUS')  \nPerson(Etternavn='OLDERVIK', " \
                  "Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948', Poststed='FEDJE')  \n"


def test_postfixOrder_linked_nodes(linked_nodes, capfd):
    root_node = linked_nodes
    root_node.postfixOrder()
    out, err = capfd.readouterr()
    assert out == "Person(Etternavn='GJERSTAD', Fornavn='TORKJELL', Adresse='HOSTELAND 2 83', Postnummer='1361', " \
                  "Poststed='ØSTERÅS')  \nPerson(Etternavn='OLDERVIK', Fornavn='SHARI LILL', Adresse='KRÆKA 84', " \
                  "Postnummer='5948', Poststed='FEDJE')  \nPerson(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', " \
                  "Adresse='LEINAHYTTA 36', Postnummer='7224', Poststed='MELHUS')  \n"


# Line 85-86 are hard to reach. It is difficult to test the functionality of a while loop without changing the code.
# The easiest test would be moving the while loop into a helper function.
def test_levelOrder_linked_nodes(linked_nodes, capfd):
    root_node = linked_nodes
    root_node.levelOrder()
    out, err = capfd.readouterr()
    assert out == "Person(Etternavn='KRISTIANSEN', Fornavn='MORTEN KRISTIAN', Adresse='LEINAHYTTA 36', " \
                  "Postnummer='7224', Poststed='MELHUS')  \nPerson(Etternavn='GJERSTAD', Fornavn='TORKJELL', " \
                  "Adresse='HOSTELAND 2 83', Postnummer='1361', Poststed='ØSTERÅS')  \nPerson(Etternavn='OLDERVIK', " \
                  "Fornavn='SHARI LILL', Adresse='KRÆKA 84', Postnummer='5948', Poststed='FEDJE')  \n"


# Testing the order functions with empty non-linked root nodes

def test_prefixOrder_empty_node(capfd):
    root_node = BinaryTreeNode(value="")
    root_node.prefixOrder()
    out, err = capfd.readouterr()
    assert out == "  \n"


def test_infixOrder_empty_node(capfd):
    root_node = BinaryTreeNode(value="")
    root_node.infixOrder()
    out, err = capfd.readouterr()
    assert out == "  \n"


def test_postfixOrder_empty_node(capfd):
    root_node = BinaryTreeNode(value="")
    root_node.postfixOrder()
    out, err = capfd.readouterr()
    assert out == "  \n"


def test_levelOrder_empty_node(capfd):
    root_node = BinaryTreeNode(value="")
    root_node.postfixOrder()
    out, err = capfd.readouterr()
    assert out == "  \n"


# While the order functions work for empty nodes they do not work for empty trees. The BinaryTree class on
# instantiation sets root to None instead of making root a BinaryTree node. This causes an Attribute error.
# Empty tree order functions marked with xfail. To avoid I suggest adding a check for root being None in the
# order functions.
@pytest.mark.xfail(raises=AttributeError)
def test_prefixOrder_empty_tree(capfd):
    test_tree_empty = BinaryTree()
    test_tree_empty._root.prefixOrder()
    # out, err = capfd.readouterr()
    # assert out == ""


@pytest.mark.xfail(raises=AttributeError)
def test_infixOrder_empty_tree(capfd):
    test_tree_empty = BinaryTree()
    test_tree_empty._root.infixOrder()
    # out, err = capfd.readouterr()
    # assert out == ""


@pytest.mark.xfail(raises=AttributeError)
def test_postfixOrder_empty_tree(capfd):
    test_tree_empty = BinaryTree()
    test_tree_empty._root.postfixOrder()
    # out, err = capfd.readouterr()
    # assert out == ""


@pytest.mark.xfail(raises=AttributeError)
def test_levelOrder_empty_tree(capfd):
    test_tree_empty = BinaryTree()
    test_tree_empty._root.levelOrder()
    # out, err = capfd.readouterr()
    # assert out == ""


def test_equality(sample_nodes, sample_persons):
    node1, node2, node3, node4, node5 = sample_nodes
    node6 = BinaryTreeNode(value=sample_persons[0])
    assert node1 == node6
    assert node1.value == node6.value
    assert not node1 == node3
    assert node5 == None
    assert not node5 == node1
    assert not node1 == node5
    assert not node1 == None


# The equality operations seem to be set up correctly, however it is bad practice to code both equality and
# inequality. The reason for this is that if you change the equality function you have to change the inequality
# function as well. It is much simpler to just code the equality function and use not equal to in the inequality
# function. In any case the inequality function is not working as intended. The code reads "return not self.value !=
# other.value". The "not" has to be removed for this part of the function to work correctly.
def test_notequal_different_nodes(sample_nodes):
    assert sample_nodes[0] != sample_nodes[1]


def test_notequal_identical_nodes(sample_persons):
    node1 = BinaryTreeNode(sample_persons[0])
    node2 = BinaryTreeNode(sample_persons[0])
    assert not node1 != node2


# Other parts of the inequality function are set up wrong as well. If other is not None but self is, it returns false
# for the unequal call.
def test_notequal_self_noneValue_other_notNone(sample_nodes):
    empty_node = BinaryTreeNode(value=None)
    assert empty_node != sample_nodes[0]


# Other's value is not checked either. And since the BinaryTreeNode class allows the use of None values it would be
# prudent to check the value.
def test_notequal_self_notNone_other_noneValue(sample_nodes):
    empty_node = BinaryTreeNode(value=None)
    assert sample_nodes[0] != empty_node


# If other node is None always returns that the 2 inputs are unequal. Which is baffling considering the equality
# function returns True for the comparison None and self.value == None. In later tests I stuck to asserting the
# outcome coded in the functions when it came to comparisons with object = None ( different to .value = None) despite
# the logical inconsistencies. (e.g. if self.value(None) == None is True, then self.value(None) <= None should be True
# as well)
def test_notequal_self_notNone_other_none(sample_nodes):
    assert not sample_nodes[4] != None


# The less than and greater than functions are simply a copy-paste of the equality function without taking into
# account that while python does allow equality and inequality comparisons with None it does not allow other
# operations like "<" or ">" and throws a TypeError exception. I would have ignored most cases of None comparisons
# and not written the tests but for the fact that a part of those comparisons were coded already so the rest has to
# be taken into account as well.
# I marked those TypeErrors with xfail
def test_less_than(sample_nodes):
    assert sample_nodes[1] < sample_nodes[0]
    assert sample_nodes[1].value < sample_nodes[0].value
    assert not sample_nodes[2] < sample_nodes[1]


@pytest.mark.xfail(raises=TypeError)
def test_less_than_selfValue_none(sample_nodes):
    assert sample_nodes[4] < sample_nodes[0]


# def test_less_than_self_none_otherValue_none(sample_nodes):
#    assert not None < sample_nodes[4]

# def test_less_than_self_none_other_none(sample_nodes):
#    assert not None < None

def test_less_than_selfValue_none_other_none(sample_nodes):
    assert not sample_nodes[4] < None


@pytest.mark.xfail(raises=TypeError)
def test_less_otherValue_none(sample_nodes):
    assert not sample_nodes[0] < sample_nodes[4]


def test_less_other_none(sample_nodes):
    assert not sample_nodes[0] < None


def test_greater_than(sample_nodes):
    assert sample_nodes[0] > sample_nodes[1]
    assert sample_nodes[0].value > sample_nodes[1].value
    assert not sample_nodes[1] > sample_nodes[2]


@pytest.mark.xfail(raises=TypeError)
def test_greater_than_selfValue_none(sample_nodes):
    assert not sample_nodes[4] > sample_nodes[0]


# def test_greater_than_self_none_otherValue_none(sample_nodes):
#     assert not None > sample_nodes[4]

# def test_greater_than_self_none_other_none(sample_nodes):
#     assert not None > None

def test_greater_than_selfValue_none_other_none(sample_nodes):
    assert not sample_nodes[4] > None


@pytest.mark.xfail(raises=TypeError)
def test_greater_otherValue_none(sample_nodes):
    assert sample_nodes[0] > sample_nodes[4]


def test_greater_other_none(sample_nodes):
    assert not sample_nodes[0] > None


def test_less_than_or_equal(sample_nodes):
    assert sample_nodes[1] <= sample_nodes[0]
    assert sample_nodes[1].value <= sample_nodes[0].value
    assert not sample_nodes[2] <= sample_nodes[1]
    assert sample_nodes[2] <= sample_nodes[2]


# Less or equal and greater or equal checks break again when basing the tests on the initial equality statement that
# None == None -> True. Both due to inconsistent logic and the NoneType comparisons Python disallows.
@pytest.mark.xfail(raises=TypeError)
def test_less_than_or_equal_selfValue_none(sample_nodes):
    assert sample_nodes[4] <= sample_nodes[0]


@pytest.mark.xfail(raises=TypeError)
def test_less_than_or_equal_selfValue_none_otherValue_none():
    node1 = BinaryTreeNode(value=None)
    node2 = BinaryTreeNode(value=None)
    assert node1 <= node2


def test_less_than_or_equal_self_not_less_none(sample_nodes):
    assert not sample_nodes[0] <= None


def test_less_than_or_equal_selfValue_none_other_none(sample_nodes):
    assert not sample_nodes[4] <= None


def test_greater_than_or_equal(sample_nodes):
    assert sample_nodes[0] >= sample_nodes[1]
    assert sample_nodes[0].value >= sample_nodes[1].value
    assert not sample_nodes[1] >= sample_nodes[2]
    assert sample_nodes[2] >= sample_nodes[2]


@pytest.mark.xfail(raises=TypeError)
def test_greater_than_or_equal_selfValue_none(sample_nodes):
    assert not sample_nodes[4] >= sample_nodes[0]


@pytest.mark.xfail(raises=TypeError)
def test_greater_than_or_equal_selfValue_none_otherValue_none():
    node1 = BinaryTreeNode(value=None)
    node2 = BinaryTreeNode(value=None)
    assert node1 >= node2


def test_greater_than_or_equal_self_not_less_none(sample_nodes):
    assert not sample_nodes[0] >= None


def test_greater_than_or_equal_selfValue_none_other_none(sample_nodes):
    assert not sample_nodes[4] >= None
