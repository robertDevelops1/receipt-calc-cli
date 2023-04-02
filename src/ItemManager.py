import Item

class ItemManager:

    def __init__(self):
        self.items = {}

    def getItems(self):
        return self.items

    def addItem(self, item:Item):
        itemId = item.getId()
        if itemId in self.items:
            print("Item registered already")
        else:
            self.items[itemId] = item
            return itemId
        
    def removeItem(self, item:Item):
        itemId = item.getId()
        id = self.items.pop(itemId)
        return id
    
    def hasItem(self, itemId:int):
        return (itemId in self.items)
    
    def getItem(self, itemId:int):
        return self.items.get(itemId)