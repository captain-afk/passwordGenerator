import random
from random import shuffle



def randomizePassword(letterCount, numberCount, symbolCount):
    newPassword = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    for x in range(letterCount):                    #Get all the random letters you need
        newPassword.append(random.choice(letters))
    for x in range(numberCount):                    #Get all the random numbers you need
        newPassword.append(random.choice(numbers))
    for x in range(symbolCount):                    #Get all the random symbols you need
        newPassword.append(random.choice(symbols))
    shuffle(newPassword)                            #Shuffle all the characters you already gathered
    return(newPassword)                             #Return as a list

def listToString(userList):                         #Input a list and return as a single concatonated string
    s = ''
    for x in userList:
        s += x
    return(s)


def main():
    print("How many letters would you like in your password?")
    letterCount = int(input())
    print("How many numbers would you like in your password?")
    numberCount = int(input())
    print("How many symbols would you like in your password?")
    symbolCount = int(input())

    newPasswordList = randomizePassword(letterCount,numberCount,symbolCount)
    newPassword = listToString(newPasswordList)
    print("Your new password is:", newPassword)

main()