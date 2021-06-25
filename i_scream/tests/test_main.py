import unittest

from src.milk_solids import MilkSolids
from src.non_fat_milk_solids import NonFatMilkSolids
from src.milk_fat import MilkFat


class MainTest(unittest.TestCase):
    def test_example1(self):
        ret = MilkSolids(NonFatMilkSolids(10), MilkFat(8))
        self.assertEqual(ret.type.value, (1))

    def test_example2(self):
        ret = MilkSolids(NonFatMilkSolids(1), MilkFat(2))
        self.assertEqual(ret.type.value, (3))

    def test_example3(self):
        ret = MilkSolids(NonFatMilkSolids(0), MilkFat(0))
        self.assertEqual(ret.type.value, (4))
