class Item:

    def __init__(self,id:int,name:str,store:str,itemCost:float,tax:float):
        self.id = id
        self.name = name
        self.store = store
        self.itemCost = itemCost
        self.tax = tax 

    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getStore(self):
        return self.store

    def getItemCost(self):
        return self.itemCost

    def getTax(self):
        return self.tax

    def __str__(self):
        string = "[ID:{0}  Name:{1}  Store:{2}  Cost:${3}  Tax:{4}%]".format(self.id,self.name,self.store,self.itemCost,self.tax)
        return string