import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_split(self):
        self.assertTupleEqual(calc.split([1, 2, 3, 4, 5]), ([1, 2], [3, 4, 5]))

    def test_merge_sorted_lists(self):
        self.assertListEqual(calc.merge_sorted_lists([1, 5], [3, 4]), [1, 3, 4, 5])

    def test_merge_sort(self):
        self.assertListEqual(calc.merge_sort([9, 1, 10, 2]), [1, 2, 9, 10])

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(-1, -1), 0)

    def test_multi(self):
        self.assertEqual(calc.multi(10, 5), 50)
        self.assertEqual(calc.multi(-1, 1), -1)
        self.assertEqual(calc.multi(-1, -1), 1)

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(-1, 1), -1)
        self.assertEqual(calc.div(-1, -1), 1)

    def test_calculation(self):
        result = calc.calculation("6", "+", "7")
        self.assertEqual(result, "6+7=")

    def test_mod(self):
        self.assertTrue(calc.mod(8, 2))
        self.assertFalse(calc.mod(7, 2))

    def test_equal(self):
        self.assertTrue(calc.equal(8, 8))
        self.assertEqual(calc.equal(4,9), 9)
        self.assertEqual(calc.equal(7, -2), 7)


if __name__ == '__main__':
    unittest.main()
