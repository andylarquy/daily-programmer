# Speed = Distance / Time Calculator

# MENU
def displayMenu():
    print('\n')
    print('1) Speed = Distance / Time')
    print('2) Time = Distance / Speed')
    print('3) Distance = Time * Speed')
    print('4) Exit')
    print('\n')


def getChoice():
    print('Select an option:')
    return int(input())
# /MENU


# OPERATIONS
def getDistance():
    print('\nEnter the distance:')
    return int(input())

def getTime():
    print('\nEnter the time:')
    return int(input())

def getSpeed():
    print('\nEnter the speed:')
    return int(input())

def getDivision(num1, num2):
    return str(round(num1 / num2, 2))

def getProduct(num1, num2):
    return str(num1 * num2)
# /OPERATIONS


choice = 0

while choice != 4:
    displayMenu()
    choice = getChoice()

    if choice == 1:
        # Calculate Speed
        print('\nThe speed is: '+getDivision(getDistance(), getTime()))

    elif choice == 2:
        # Calculate Time
        print('\nThe time is: '+getDivision(getDistance(), getSpeed()))

    elif choice == 3:
        # Calculate Distance
        print('\nThe distance is: '+getProduct(getTime(), getSpeed()))

print('\nBye!')