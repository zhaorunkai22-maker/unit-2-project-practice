class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item_name):
        for item in self._items:
            if item._name == item_name:
                self._items.remove(item)
                return item
        return None
    
    def __str__(self):
        if not self._items:
            return "Inventory is empty"
        result = ""
        for item in self._items:
            result += str(item)  
        return result