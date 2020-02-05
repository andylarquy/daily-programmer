def getOption():
    option = 0
    while(option < 1 or option > 3):
        print('\n')
        print('1) No! My number is higher!')
        print('2) Yes! You guessed correctly!!')
        print('3) No! My number is lower!')
        option = int(input())
    return option


# Initial Values
top = 101
base = 1
option = 0

print('\nChoice a number between '+str(base)+' and ' + str(top - 1) + " and don't forget it.\n")


while(option != 2):

    guess = int((base + top) / 2)
    
    print('Your number is ' + str(guess) +'?')
    option = getOption()

    if (option == 1):
       base = guess

    elif (option == 3):
        top = guess
        
print('\nBye!')