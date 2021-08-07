from enum import Enum

class HypeSquad(Enum):

    BRAVERY = 1
    BRILLIANCE = 2
    BALANCE = 3

    @staticmethod
    def get_by_value(value: int):
        return ([i for i in HypeSquad if i.value == value])[0]

    @staticmethod
    def keys():
        return list(map(lambda i: i.name, HypeSquad))

    @staticmethod
    def values():
        return list(map(lambda i: i.value, HypeSquad))