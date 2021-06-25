import unittest
from src.milk_solids import MilkSolids, IceType
from src.non_fat_milk_solids import NonFatMilkSolids
from src.milk_fat import MilkFat


class MilkSolidsTest(unittest.TestCase):
    def test_shouldThrow_whenSumOfNonFatMilkSolidsAndMilkFatIsGreaterThan100(self):
        with self.assertRaises(RuntimeError):
            MilkSolids(NonFatMilkSolids(100), MilkFat(1))

    def test_shouldBeIceCream(self):
        milk_solids = 15
        milk_fat = 8
        non_fat_milk_solids = milk_solids - milk_fat

        ret = MilkSolids(NonFatMilkSolids(non_fat_milk_solids), MilkFat(milk_fat))
        self.assertEqual(ret.type, IceType.ICE_CREAM)

    def test_shouldBeIceMilk(self):
        for milk_solids, milk_fat in ((10, 3), (14, 13), (10, 7)):
            with self.subTest(milk_solids=milk_solids, milk_fat=milk_fat):
                non_fat_milk_solids = milk_solids - milk_fat
                ret1 = MilkSolids(NonFatMilkSolids(non_fat_milk_solids), MilkFat(milk_fat))
                self.assertEqual(ret1.type, IceType.ICE_MILK)

    def test_shouldBeLactoIce(self):
        for milk_solids, milk_fat in ((3, 3), (3, 0), (15, 2)):
            with self.subTest(milk_solids=milk_solids, milk_fat=milk_fat):
                non_fat_milk_solids = milk_solids - milk_fat
                ret1 = MilkSolids(NonFatMilkSolids(non_fat_milk_solids), MilkFat(milk_fat))
                self.assertEqual(ret1.type, IceType.LACTO_ICE)

    def test_shouldBeFrozenDessert(self):
        for milk_solids, milk_fat in ((2, 2), (2, 0)):
            with self.subTest(milk_solids=milk_solids, milk_fat=milk_fat):
                non_fat_milk_solids = milk_solids - milk_fat
                ret1 = MilkSolids(NonFatMilkSolids(non_fat_milk_solids), MilkFat(milk_fat))
                self.assertEqual(ret1.type, IceType.FROZEN_DESSERT)
