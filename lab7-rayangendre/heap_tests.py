import unittest
from heap import *


class TestHeap(unittest.TestCase):

    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_04_build_heap(self):
        test_heap = MaxHeap(10)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(2)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])

    def test_all(self):
        my_heap = MaxHeap(5)
        self.assertEqual(my_heap.peek(), None)
        self.assertEqual(my_heap.dequeue(), None)
        self.assertTrue(my_heap.is_empty())
        self.assertFalse(my_heap.is_full())
        self.assertEqual(my_heap.get_capacity(), 5)
        self.assertEqual(my_heap.get_size(), 0)

        self.assertTrue(my_heap.enqueue(10))
        self.assertTrue(my_heap.enqueue(30))
        self.assertTrue(my_heap.enqueue(40))
        self.assertTrue(my_heap.enqueue(5))
        self.assertTrue(my_heap.enqueue(15))
        self.assertFalse(my_heap.enqueue(100))
        self.assertFalse(my_heap.is_empty())
        self.assertTrue(my_heap.is_full())
        self.assertEqual(my_heap.get_size(), 5)

        self.assertEqual(my_heap.peek(), 40)
        self.assertEqual(my_heap.dequeue(), 40)
        self.assertEqual(my_heap.contents(), [30, 15, 10, 5])

        my_heap.build_heap([2, 4, 6, 8, 10, 12, 14])
        self.assertEqual(my_heap.contents(), [14, 10, 12, 8, 4, 2, 6])

        test_array = []
        for i in range(20, 0, -1):
            test_array.append(i)
        temp = test_array
        my_heap.heap_sort_ascending(test_array)
        temp.sort()
        self.assertEqual(test_array, temp)
        self.assertEqual(my_heap.contents(), [20, 19, 15, 18, 11, 13, 14, 17, 9, 10, 2, 12, 6, 3, 7, 16, 8, 4, 1, 5])


if __name__ == "__main__":
    unittest.main()