from character import Wizard, Warrior, Character
from items import Weapon, Potion


# polymorphism function  
def make_attack(character):
    print(character.attack())


def main():
    # Create characters
    wizard = Wizard("Gandalf", 100, 50)
    warrior = Warrior("Thor", 150, 80)

    # Create items
    sword = Weapon("Sword", 5, 20)
    potion = Potion("Health Potion", 1., 30)

    # Equip weapon
    wizard.set_weapon(sword)
    warrior.set_weapon(sword)

    # Add potion to inventory
    wizard.get_inventory().add_item(potion)
    warrior.get_inventory().add_item(potion)

    # Show polymorphism
    make_attack(wizard)
    make_attack(warrior)

    # Show inventory
    print("Wizard Inventory:", wizard.get_inventory())
    print("Warrior Inventory:", warrior.get_inventory())

    # Show class attribute
    print("Total characters:", Character.get_character_count())


main()