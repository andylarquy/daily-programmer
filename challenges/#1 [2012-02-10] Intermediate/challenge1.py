# OOP

# Singleton
class Schedule(object):
    __instance = None
    events = []

    def __new__(cls):
        if Schedule.__instance is None:
            Schedule.__instance = object.__new__(cls)
        return Schedule.__instance

class Event:
    description = ''
    hour = None

    def __init__(self, description, hour):
        self.description = description
        self.hour = hour
# /OOP

# Functions
def displayMenu():
    print('1) Add new Event.')
    print('2) Edit an Event.')
    print('3) Delete an Event.')
    print('4) List Events.')
    print('5) Exit.')


def getChoiceByUser():
    choice = 0
    while ((choice < 1) or (choice > 5)):
        print('Select an option:')
        choice = int(input())
    return choice


def getEventDetails():

    print('Give your event a description')
    description = input()

    print('\n')

    print('Give your event an hour (HH:mm)')
    hour = input()

    return description, hour


def displayEvents():
    schedule = Schedule()

    print('Current events: ')

    for i in range(0, len(schedule.events)):
        print(str(i)+') '+schedule.events[i].description+' - '+schedule.events[i].hour)
    
    print('\n')


def getOptionByUser():
    option = -1
    schedule = Schedule()
    while ((option < 0) or (option >= len(schedule.events))):
        print('Select an option:')
        option = int(input())
    return option


def editEventWithIndex(index):
    schedule = Schedule()
    description, hour = getEventDetails()

    schedule.events[index].description = description
    schedule.events[index].hour = hour

    print('Your event has been edited succesfuly!')
    print('\n')


def deleteEventWithIndex(index):
    schedule = Schedule()
    schedule.events.pop(index)

    print('Your event has been deleted succesfuly!')
    print('\n')


def addNewEvent():
    
    schedule = Schedule()

    description, hour = getEventDetails()
    schedule.events.append(Event(description, hour))
    print('\n')
    
    print('Your event has been added succesfuly!')

    print('\n')


def deleteEvent():
    displayEvents()
    option = getOptionByUser()
    deleteEventWithIndex(option)


def editEvent():
    displayEvents()
    option = getOptionByUser()
    editEventWithIndex(option)



# /Functions

#Initial Declarations
choice = None
schedule = Schedule()

print('Welcome!\n')
while (choice != 5):
    displayMenu()
    choice = getChoiceByUser()
    print('\n')
    
    if choice == 1:
        addNewEvent()
    
    elif choice == 2:
        editEvent()
    
    elif choice == 3:
        deleteEvent()

    elif choice == 4:
        displayEvents()

print('Bye!')
