import unittest
from src.milk_fat import MilkFat


class MilkFatTest(unittest.TestCase):
    def test_shouldThrow_whenLessThan0(self):
        with self.assertRaises(RuntimeError):
            MilkFat(-1)

    def test_shouldThrow_whenGreaterThan100(self):
        with self.assertRaises(RuntimeError):
            MilkFat(101)

    def test_shouldThrow_whenFloatValue(self):
        with self.assertRaises(RuntimeError):
            MilkFat(0.1)

    def test_shouldHaveValue_whenBeBetween0and100(self):
        ret1 = MilkFat(0)
        self.assertEqual(ret1.value, 0)

        ret2 = MilkFat(100)
        self.assertEqual(ret2.value, 100)
