class User:

    def __init__(self,id:int, name:float):
        self.id = id
        self.name = name
        self.total = 0

    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getTotal(self):
        return self.total

    def __str__(self):
        return self.name