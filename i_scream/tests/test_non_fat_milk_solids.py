import unittest
from src.non_fat_milk_solids import NonFatMilkSolids


class NonFatMilkSolidsTest(unittest.TestCase):
    def test_shouldThrow_whenLessThan0(self):
        with self.assertRaises(RuntimeError):
            NonFatMilkSolids(-1)

    def test_shouldThrow_whenGreaterThan100(self):
        with self.assertRaises(RuntimeError):
            NonFatMilkSolids(101)

    def test_shouldThrow_whenFloatValue(self):
        with self.assertRaises(RuntimeError):
            NonFatMilkSolids(0.1)

    def test_shouldHaveValue_whenBeBetween0and100(self):
        ret1 = NonFatMilkSolids(0)
        self.assertEqual(ret1.value, 0)

        ret2 = NonFatMilkSolids(100)
        self.assertEqual(ret2.value, 100)
