from enum import Enum


class AutoName(Enum):
    def describe(self):
        return self.name

    def __str__(self):
        return self.describe()


class Day(AutoName):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7
