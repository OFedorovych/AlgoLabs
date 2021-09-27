import unittest
from binary_tree import *

class TestSearchMethod(unittest.TestCase):

    def test_inserting(self):
        tree = Tree()
        tree.insert(15)
        tree.insert(20)
        tree.insert(10)
        self.assertEqual(tree.root.value, 15)
        self.assertEqual(tree.root.left.value, 10)
        self.assertEqual(tree.root.right.value, 20)

    def test_searching(self):
        tree = Tree()
        tree.insert(22)
        tree.insert(14)
        tree.insert(15)
        tree.insert(86)
        self.assertEqual(tree.search(86), True)
        self.assertEqual(tree.search(12), False)

    def test_delete(self):
        tree = Tree()
        tree.insert(15)
        tree.insert(20)
        tree.insert(17)
        tree.insert(10)
        tree.delete(15)
        self.assertNotEqual(tree.root.value, 15)
        self.assertEqual(tree.root.value, 17)
        self.assertEqual(tree.root.right.value, 20)
        self.assertEqual(tree.root.left.value, 10)

    def test_find_item(self):
        tree = Tree()
        tree.insert(15)
        tree.insert(20)
        tree.insert(17)
        tree.insert(10)
        self.assertEqual(tree.find_item(10).value, 10)


if __name__ == "__main__":
    unittest.main()