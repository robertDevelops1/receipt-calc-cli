import Assignment
import Item
import User


class AssignmentManager:

    def __init__(self):
        """creates an empty dictionary 
            key: assignment code
            value: Assignment
        """        
        self.assignments = {}
    
    def getAssignments(self):
        return self.assignments

    def addAssignment(self,user:User,item:Item):
        newAssignment = Assignment(user,item)
        keyCode = repr(newAssignment)
        if keyCode in self.assignments:  
            print("Assignment already exists")
        else: 
            self.assignments[keyCode] = newAssignment

    def removeAssignment(self,user:User,item:Item):
        theAssignment = Assignment(user,item)
        keyCode = repr(theAssignment)
        # if keyCode in self.assignments:
        #     del self.assignments[keyCode]
        # else:
        #     print("Assignment does not exist")
        id = self.assignments.pop(keyCode)
        return id