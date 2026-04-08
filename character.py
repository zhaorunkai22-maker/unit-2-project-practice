from abc import ABC, abstractmethod
from inventory import Inventory


class Character(ABC):
    _character_count = 0  # class attribute

    def __init__(self, name:str, hp:int):
        self._name = name
        self._hp = self._validate_hp(hp)
        self._weapon = None  # composition
        self._inventory = Inventory()  # composition

        Character._character_count += 1

    
    def _validate_hp(self, hp:int):
        if hp <= 0:
            raise ValueError("HP must be positive.")
        return hp

    
    def set_weapon(self, weapon):
        self._weapon = weapon

    def get_inventory(self):
        return self._inventory

    
    @classmethod
    def get_character_count(cls):
        return cls._character_count
    

    @abstractmethod
    def attack(self):
        pass

    def __str__(self):
        return f"{self._name} (HP: {self._hp})"

    



class Wizard(Character):
    def __init__(self, name:str, hp:int, mana:int):
        super().__init__(name, hp)
        self._mana = mana

    def attack(self):
        if self._weapon:
            return f"{self._name} casts a spell with {self._weapon._name}!"
        return f"{self._name} casts a basic spell!"



class Warrior(Character):
    def __init__(self, name:str, hp:int, rage:int):
        super().__init__(name, hp)
        self._rage = rage

    def attack(self):
        if self._weapon:
            return f"{self._name} strikes with {self._weapon._name}!"
        return f"{self._name} punches with rage!"