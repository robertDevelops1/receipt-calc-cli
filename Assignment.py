from Item import Item
from User import User


class Assignment:

    def __init__(self,user:User,item:Item):
        self.user = user
        self.item = item

    def getUser(self):
        return self.user
    
    def getItem(self):
        return self.item
    
    def __repr__(self):
        string = "u{0}i{1}".format(self.user.getId,self.item.getId)
        return string