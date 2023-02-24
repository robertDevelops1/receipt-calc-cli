import User


class UserManager:

    def __init__(self):
        self.users = {}

    def getUsers(self):
        return self.users

    def addUser(self, user:User):
        userId = user.getId()
        if userId in self.users:
            print("User registered already")
        else:
            self.users[userId] = user
            return userId
        
    def removeUser(self,user:User):
        userId = user.getId()
        id = self.users.pop(userId)
        return id