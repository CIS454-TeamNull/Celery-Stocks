from datetime import datetime

celery = {}
print(celery)

# Resource I used to get the time
# https://realpython.com/python-get-current-time/
dateToday = str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)
print(dateToday)

def insertItem(item, values):
    celery.update({item : values})

def updateQuantity(item, quantity):
    celery[item][1] = quantity

def updateStoreDate(item, storeDate):
    celery[item][2] = storeDate

def updateExpirationDate(item, expirationDate):
    celery[item][3] = expirationDate

def removeItem(target):
    del celery[target]