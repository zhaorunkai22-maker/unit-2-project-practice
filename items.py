from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    @abstractmethod
    def use(self):
        pass

    def __str__(self):
        return f"{self._name} (Weight: {self._weight})"



class Weapon(Item):
    def __init__(self, name, weight, damage):
        super().__init__(name, weight)
        self._damage = damage

    def use(self):
        return f"Weapon deals {self._damage} damage"
    



class Potion(Item):
    def __init__(self, name, weight, healing):
        super().__init__(name, weight)
        self._healing = healing

    def use(self):
        return f"Potion heals {self._healing} HP"

