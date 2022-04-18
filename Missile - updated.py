import math
print('It is a very windy day, missiles in this simulator only have a 75% chance of actually hitting.')
#inputs
try:
    height = float(input('Enter Height: '))
    angle = float(input('Enter Angle: '))
    amountFired = float(input('Enter amount of missiles fired: '))
#failsafe
except ValueError:
    print('Error! Enter only numbers')
#Calculations / conversions
angleR = ((math.pi/180) * angle)
distance = (height / math.sin(angleR))
hitsCalc = (amountFired * .75)
cost = (amountFired * 5000)
#final print
print('The missile must travel ',distance,'KM to reach your given height & angle')
print('out of',amountFired,'missiles fired, only',hitsCalc,'missiles will make contact. Your total cost of attack is $',cost,'.')
