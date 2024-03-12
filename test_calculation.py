import unittest
from calculation import calculate_stats


class TestCalculateStats(unittest.TestCase):

    def test_empty_list(self):
        empty_list = []
        with self.assertRaises(ValueError):
            calculate_stats(empty_list)

    def test_single_value_list(self):
        single_value_list = [5]
        self.assertEqual(
            calculate_stats(single_value_list), {"mean": 5, "median": 5, "std_dev": 0}
        )

    def test_list(self):
        list_of_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(
            calculate_stats(list_of_values),
            {
                "mean": 5.5,
                "median": 5.5,
                "std_dev": 2.8722813232690143,
            },
        )


if __name__ == "__main__":
    unittest.main()
