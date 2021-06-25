from enum import Enum
from src.milk_fat import MilkFat
from src.non_fat_milk_solids import NonFatMilkSolids


class IceType(Enum):
    ICE_CREAM = 1
    ICE_MILK = 2
    LACTO_ICE = 3
    FROZEN_DESSERT = 4


class MilkSolids:
    non_fat_milk_solids: NonFatMilkSolids
    milk_fat: MilkFat
    type: IceType

    def __init__(self, non_fat_milk_solids: NonFatMilkSolids, milk_fat: MilkFat) -> None:
        if (non_fat_milk_solids.value + milk_fat.value > 100):
            raise RuntimeError

        self.non_fat_milk_solids = non_fat_milk_solids
        self. milk_fat = milk_fat
        self.type = self.__classify(non_fat_milk_solids.value, milk_fat.value)

    def __classify(self, non_fat_milk_solids: int, milk_fat: int) -> IceType:
        milk_solids = non_fat_milk_solids + milk_fat
        if (milk_solids >= 15 and milk_fat >= 8):
            return IceType.ICE_CREAM
        elif(milk_solids >= 10 and milk_fat >= 3):
            return IceType.ICE_MILK
        elif(milk_solids >= 3):
            return IceType.LACTO_ICE
        else:
            return IceType.FROZEN_DESSERT
