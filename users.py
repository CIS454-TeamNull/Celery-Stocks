items = {}

# Resource I used for the objects
# https://www.w3schools.com/python/python_classes.asp
class User:
    def _init_(self, username, password, address, employeeId, phoneNumber, role):
        self.username = username
        self.password = password
        self.address = address
        self.employeeId = employeeId
        self.phoneNumber = phoneNumber
        self.role = role

#This class will get the ingredients from the menu item, go into the data base and minus the correct quantity from the data base
class Waiter(User):
    def sellItem(menuItem):
        for ingredients in items[menuItem]:
            return ingredients

#This class will create a different dictionary that holds the menu item and what ingredients they use    
class Chef(User):
    def createItem(menuItem, ingredients):
        items.update({menuItem : ingredients})