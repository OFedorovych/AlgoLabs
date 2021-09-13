import unittest
from heap_sort import *

class TestHeapSort(unittest.TestCase):

    def test_sorting_ascend(self):
        self.assertAlmostEqual(Heapsort([1, 87, 15, 4, -20, 115], "asc"), [-20, 1, 4, 15, 87, 115])
    
    def test_sorting_descend(self):
        self.assertAlmostEqual(Heapsort([1, 87, 15, 4, -20, 115], "desc"), [115, 87, 15, 4, 1, -20])




if __name__ == '__main__':
    unittest.main()