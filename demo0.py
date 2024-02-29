from datetime import datetime

celery = {}

# When implementing time, it must be in the format of month/date/year.
# For months that have numbers between 1-9, they have to be implemented as 1-9 instead of 01-09. Ex. Jan is 1 not 01.
# For months that have numbers between 10-12, they have to be implemented as 10-12. Ex. December is 12.
# Resource I used to get the time
# https://realpython.com/python-get-current-time/
dateToday = str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)
print(dateToday)

def insertItem(item, values):
    celery.update({item : values})

def updateQuantity(item, quantity):
    celery[item][0] = quantity

def updateStoreDate(item, storeDate):
    celery[item][1] = storeDate

def updateExpirationDate(item, expirationDate):
    celery[item][2] = expirationDate

def removeItem(item):
    del celery[item]

# Resource I used to implement celery.item()
# https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/
def expirationAlert():
    for i, j in celery.items():
        if(dateToday == j[2]):
            print(i + " is expired!!!")

#Test
print(celery)
insertItem("celery", [5, "1/1/2024", "2/27/2024"])
print(celery)
updateQuantity("celery", 10)
print(celery)
updateStoreDate("celery", "2/5/2024")
print(celery)
expirationAlert()
updateExpirationDate("celery", "2/28/2024")
print(celery)
expirationAlert()