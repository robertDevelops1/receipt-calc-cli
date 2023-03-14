import Item

class ItemCostManager:

    def __init__(self):
        """creates an empty dictionary 
            key: itemId
            value: cost per user
        """        
        self.items = {}

    def getItems(self):
        return self.items

    def addItem(self,item:Item):
        itemId = item.getId()
        itemCost = item.getItemCost()
        if itemId in self.items:
            numberOfUsers = round(itemCost / self.items[itemId]) + 1        # +1 user
            newCostPerUser = round((itemCost / numberOfUsers),2)
            self.items[itemId] = newCostPerUser
        else:
            self.items[itemId] = itemCost       #cost per user of Item cost

    def removeItem(self,item:Item):
        itemId = item.getId()
        itemCost = item.getItemCost()
        if itemId in self.items:
            numberOfUsers = round(itemCost / self.items[itemId]) - 1        # -1 user
            newCostPerUser = round((itemCost / numberOfUsers),2)
            self.items[itemId] = newCostPerUser
        else:
            print("Item does not exist")