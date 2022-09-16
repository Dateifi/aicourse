from BTtests.BinaryTreeNode import BinaryTreeNode
from BTtests.BinaryTree import BinaryTree
import unittest
from collections import namedtuple


class BinaryTreeNodeTests(unittest.TestCase):
    def setUp(self):
        self.person = namedtuple('Person', ["Etternavn", "Fornavn", "Adresse", "Postnummer", "Poststed"])
        person1 = self.person("KRISTIANSEN", "MORTEN KRISTIAN", "LEINAHYTTA 36", "7224", "MELHUS")
        person2 = self.person("OLDERVIK", "SHARI LILL", "KRÆKA 84", "5948", "FEDJE")
        self.node1 = BinaryTreeNode(value=person1, lefttree=1, righttree=None)
        self.node2 = BinaryTreeNode(value=person2, lefttree=None, righttree=1)
        self.node3 = BinaryTreeNode(value=None, lefttree=None, righttree=None)


    def tearDown(self) -> None:
        self.node1 = None
        self.node2 = None
        self.node3 = None

    def test_init(self):
        self.assertEqual(self.node1.value,
                         self.person("KRISTIANSEN", "MORTEN KRISTIAN", "LEINAHYTTA 36", "7224", "MELHUS"))
        self.assertEqual(self.node1.left, 1)
        self.assertEqual(self.node1.right, None)
        self.assertEqual(self.node2.value, self.person("OLDERVIK", "SHARI LILL", "KRÆKA 84", "5948", "FEDJE"))
        self.assertEqual(self.node2.left, None)
        self.assertEqual(self.node2.right, 1)

    def test_hasRight(self):
        self.assertEqual(self.node1.hasRight(), False)
        self.assertEqual(self.node2.hasRight(), True)

    def test_hasLeft(self):
        self.assertEqual(self.node1.hasLeft(), True)
        self.assertEqual(self.node2.hasLeft(), False)

    def test_prefixOrder(self):
        pass

    def test_infixOrder(self):
        pass

    def test_postfixOrder(self):
        pass

    def test_levelOrder(self):
        pass

    def test_levelOrderEntry(self):
        pass

    def test_node_equality(self):
        self.assertEqual(self.node1, self.node1)
        self.assertNotEqual(self.node1, None)

    def test_node_inequality(self):
        self.assertNotEqual(self.node3, None)
        self.assertNotEqual(self.node2, None)
        self.assertNotEqual(self.node1, self.node2)

    def test_node_less_than(self):
        self.assertLess(self.node1, self.node2)
        self.assertFalse(self.node2 < None)

    def test_node_greater_than(self):
        self.assertGreater(self.node2, self.node1)
        self.assertFalse(self.node1 > None)

    def test_node_less_than_or_equal(self):
        self.assertLessEqual(self.node1, self.node2)
        self.assertLessEqual(self.node1, self.node1)
        self.assertFalse(self.node2 <= None)

    def test_node_greater_than_or_equal(self):
        self.assertGreaterEqual(self.node2, self.node1)
        self.assertGreaterEqual(self.node2, self.node2)
        self.assertFalse(self.node1 >= None)


class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.person = namedtuple('Person', ["Etternavn", "Fornavn", "Adresse", "Postnummer", "Poststed"])
        self.binary_tree = BinaryTree()
        self.binary_tree_empty = BinaryTree()
        with open("Personer15.dta", "r") as file:
            for line in file:
                person = self.person(*line.strip().split(';'))
                self.binary_tree.insert(value=person)

    def tearDown(self) -> None:
        self.binary_tree = None
        self.binary_tree_empty = None

    def test_init(self):
        self.assertEqual(self.binary_tree_empty._root, None)

    def test_insert(self):
        self.binary_tree_empty.insert(
            value=self.person("KRISTIANSEN", "MORTEN KRISTIAN", "LEINAHYTTA 36", "7224", "MELHUS"))
        self.assertEqual(self.binary_tree_empty._root.value,
                         self.person("KRISTIANSEN", "MORTEN KRISTIAN", "LEINAHYTTA 36", "7224", "MELHUS"))
        self.binary_tree_empty.insert(value=self.person("OLDERVIK", "SHARI LILL", "KRÆKA 84", "5948", "FEDJE"))
        self.assertEqual(self.binary_tree._root.right.value,
                         self.person("OLDERVIK", "SHARI LILL", "KRÆKA 84", "5948", "FEDJE"))
        self.binary_tree_empty.insert(value=self.person("ELI", "RITA HELEN", "MEHEIAVEGEN 80", "4436", "GYLAND"))
        self.assertEqual(self.binary_tree_empty._root.left.value,
                         self.person("ELI", "RITA HELEN", "MEHEIAVEGEN 80", "4436", "GYLAND"))
        self.assertRaises(Exception, self.binary_tree_empty.insert,
                          self.person("ELI", "RITA HELEN", "MEHEIAVEGEN 80", "4436", "GYLAND"))
        self.assertRaises(Exception, self.binary_tree_empty.insert, None)

    def test_findLeftMost(self):
        self.assertEqual(self.binary_tree.findLeftMost(self.binary_tree._root).value,
                         self.person("ADOLFSEN", "HACI", "VEDVIKA 94", "1431", "ÅS"))

    def test_findRightMost(self):
        self.assertEqual(self.binary_tree.findRightMost(self.binary_tree._root).value,
                         self.person("ØSTBY", "FRANK", "WÅRSETH 57", "7414", "TRONDHEIM"))

    def test_findMin(self):
        self.assertEqual(self.binary_tree.findMin(), self.person("ADOLFSEN", "HACI", "VEDVIKA 94", "1431", "ÅS"))

    def test_findMax(self):
        self.assertEqual(self.binary_tree.findMax(), self.person("ØSTBY", "FRANK", "WÅRSETH 57", "7414", "TRONDHEIM"))

    def test_find(self):
        self.assertEqual(self.binary_tree.find(self.person("ADOLFSEN", "HACI", "VEDVIKA 94", "1431", "ÅS")),
                         self.person("ADOLFSEN", "HACI", "VEDVIKA 94", "1431", "ÅS"))
        self.assertEqual(self.binary_tree.find(self.person("ØSTBY", "FRANK", "WÅRSETH 57", "7414", "TRONDHEIM")),
                         self.person("ØSTBY", "FRANK", "WÅRSETH 57", "7414", "TRONDHEIM"))
        self.assertEqual(self.binary_tree.find(self.person("ELI", "RITA HELEN", "MEHEIAVEGEN 80", "4436", "GYLAND")),
                         None)
        self.assertEqual(self.binary_tree.find(None), None)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
