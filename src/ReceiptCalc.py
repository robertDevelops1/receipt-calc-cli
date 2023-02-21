from AssignmentManager import AssignmentManager
from User import User


class ReceiptCalc: 

    def getAllItems(user:User, assignmentManager:AssignmentManager):
        """retrieves all items assigned to given user from a manager

        Args:
            user (User): user to search for
            assignmentManager (AssignmentManager): manager of all assignments

        Returns:
            list(Items): items
        """        
        items = []
        allAssignments = assignmentManager.getAssignments()
        for assignment in allAssignments:
            assignmentUser = assignment.getUser()
            if assignmentUser == user:
                item = assignment.getItem()
                items.append(item)
        return items

    def getUserTotal(user:User):
        pass

