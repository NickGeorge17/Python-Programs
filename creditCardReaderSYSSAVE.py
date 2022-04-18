import math
import sys

file1 = open('creditCards.txt',"r")
stdoutOrigin=sys.stdout
sys.stdout = open('CreditCardLog.txt',"w")

count = 0
for line in file1:
    count = count + 1
file1.close()
#display count lines for number of cards per batch
file1 = open('creditCards.txt',"r")
print('Line count:', count)
file1.close()

#grab contents from file1, read them per line and find if they're 16 characters
file1 = open('creditCards.txt',"r")
for line in file1.readlines():
#converting line variable to different types to use effectively
    intLine = int(line)
    lenLine = len(line)

#getting first digit for card identify
    digits = int(math.log10(intLine))
    firstDigit = int(intLine / pow(10, digits))

#length reader to get valid cards
    if len(line) == 17:
        write = print('Valid card length accepted', line)
    elif len(line) > 17:
        print('Invalid card length', line)
    elif len(line) < 17:
        print('Invalid card length', line)
#uses firstDigit function to determine what type of card is entered per line
    if firstDigit == 3:
        print('American Express')
    elif firstDigit == 4:
        print('Visa')
    elif firstDigit == 5:
        print('Mastercard')
    elif firstDigit == 6:
        print('Discover')
    elif firstDigit > 6:
        print('Unrecognized card class, DO NOT USE.')
    elif firstDigit < 3:
        print('Unrecognized card class, DO NOT USE.')

sys.stdout.close()
file1.close()

#to get the credit card list, I used a random number generator
#source of calculous problem below.
#Know Program. (n.d.). How to get the First Digit of a Number in Python. In knowprogram.com. Retrieved March 21, 2022, from https://www.knowprogram.com/python/get-first-digit-of-number-python/
