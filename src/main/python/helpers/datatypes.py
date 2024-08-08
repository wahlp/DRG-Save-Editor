from dataclasses import dataclass, field

from helpers.enums import Category, Dwarf, Status


@dataclass
class Cost:
    """Crafting cost associated with a forgeable item"""

    credits: int = 0
    bismor: int = 0
    croppa: int = 0
    enor: int = 0
    jadiz: int = 0
    magnite: int = 0
    umanite: int = 0

    def __add__(self, other):
        newcost = Cost()
        for key in self.__dict__.keys():
            try:
                newcost.__dict__[key] = self.__dict__[key] + other.__dict__[key]
            except KeyError:
                pass
        return newcost


@dataclass()
class Item:
    """An item read from the known list of GUIDs"""

    category: Category
    dwarf: Dwarf
    name: str
    cost: dict = field(default_factory=dict)
    weapon: str | None = None
    status: Status = Status.UNACQUIRED
