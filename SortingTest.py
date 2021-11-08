import unittest
from Sorting import *
class SortingTest(unittest.TestCase):
    def test_insertion_sort(self):
        input_array = [3, 6, 1]
        sorting = Sorting(input_array)
        sorting.insertion_sort()
        self.assertEqual(sorting.sorting_array,[1, 3, 6])
        self.assertEqual(sorting.comparison_count, 3)

        input_array = [1, 2, 3, 4]
        sorting = Sorting(input_array)
        sorting.insertion_sort()
        self.assertEqual(sorting.sorting_array,[1, 2, 3, 4])
        self.assertEqual(sorting.comparison_count, 3)

    def test_merge_sort(self):
        input_array = [3, 6, 1]
        sorting = Sorting(input_array)
        sorting.merge_sort(0, len(input_array)-1)
        self.assertEqual(sorting.sorting_array,[1, 3, 6])
        self.assertEqual(sorting.comparison_count, 5)

        input_array = [1, 2, 3, 4]
        sorting = Sorting(input_array)
        sorting.merge_sort(0, len(input_array)-1)
        self.assertEqual(sorting.sorting_array,[1, 2, 3, 4])
        self.assertEqual(sorting.comparison_count, 8)


    def test_heap_sort(self):
        input_array = [3, 6, 1]
        sorting = Sorting(input_array)
        sorting.heap_sort()
        self.assertEqual(sorting.sorting_array,[1, 3, 6])
        self.assertEqual(sorting.comparison_count, 3)


        input_array = [1, 2, 3, 4]
        sorting = Sorting(input_array)
        sorting.heap_sort()
        self.assertEqual(sorting.sorting_array,[1, 2, 3, 4])
        self.assertEqual(sorting.comparison_count, 7)



if __name__ == '__main__':
    unittest.main()
