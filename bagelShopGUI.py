#Bonnies bagel shop
#I did this program in blocks of different functions so if you're trying to pick it apart, inputs are in a seperate block from outputs
from graphics import *

win = GraphWin('Its bagel time', 750, 650)
win.setCoords(0.0, 0.0, 4.0, 4.0)
win.setBackground('white')

#Interface image
image = Image(Point(2,2),'bagel_PNG61.png')
image.draw(win)

#Draw Interface
message1 = Text(Point(1.5,3), 'Whats your name:').draw(win)
message1.setTextColor('black')
message1.setStyle('bold')

message2 = Text(Point(1.5,2.85), 'Input 0 For Things You Dont Want').draw(win)
message2.setTextColor('black')
message2.setStyle('bold')

#EVERYTHING
bagel1 = Text(Point(1.5,2.5), 'How Many Everything Bagels').draw(win)
bagel1.setTextColor('black')
bagel1.setStyle('bold')

#PLAIN
bagel2 = Text(Point(1.5,2.32), 'How Many Plain Bagels').draw(win)
bagel2.setTextColor('black')
bagel2.setStyle('bold')

#MULTIGRAIN
bagel3 = Text(Point(1.5,2.15), 'How Many Multigrain Bagels').draw(win)
bagel3.setTextColor('black')
bagel3.setStyle('bold')

coffeemsg = Text(Point(1.5,2), 'Coffee').draw(win)
coffeemsg.setTextColor('black')
coffeemsg.setStyle('bold')

message3 = Text(Point(1.5,0.5), '').draw(win)
message3.setTextColor('black')
message3.setStyle('bold')

#inputName
inputName = Entry(Point(2.8,3), 8)
inputName.setText('Name')
inputName.draw(win)

#inputEverything + cheese butter
inputBagel1 = (Entry(Point(2.8,2.5), 8))
inputBagel1.setText('Everything')
inputBagel1.draw(win)
inputCheese1 = (Entry(Point(3.35,2.5), 14))
inputCheese1.setText('Cream cheese?')
inputCheese1.draw(win)
inputButter1 = (Entry(Point(3.8,2.5), 6))
inputButter1.setText('Butter?')
inputButter1.draw(win)

#inputPlain + cheese butter
inputBagel2 = (Entry(Point(2.8,2.32), 8))
inputBagel2.setText('Plain')
inputBagel2.draw(win)
inputCheese2 = (Entry(Point(3.35,2.32), 14))
inputCheese2.setText('Cream cheese?')
inputCheese2.draw(win)
inputButter2 = (Entry(Point(3.8,2.32), 6))
inputButter2.setText('Butter?')
inputButter2.draw(win)

#inputMultigrain + cheese butter
inputBagel3 = (Entry(Point(2.8,2.15), 8))
inputBagel3.setText('Multigrain')
inputBagel3.draw(win)
inputCheese3 = (Entry(Point(3.35,2.15), 14))
inputCheese3.setText('Cream cheese?')
inputCheese3.draw(win)
inputButter3 = (Entry(Point(3.8,2.15), 6))
inputButter3.setText('Butter?')
inputButter3.draw(win)

#regular or decaf coffee
inputCoffee1 = (Entry(Point(2.8,2), 8))
inputCoffee1.setText('Regular')
inputCoffee1.draw(win)

inputCoffee2 = (Entry(Point(3.35,2), 8))
inputCoffee2.setText('Decaf')
inputCoffee2.draw(win)

#Add road trip button & rectangle
button = Text(Point(2,1.5), 'Calculate')
button.setTextColor('black')
button.setStyle('bold')
button.draw(win)
rectangle = Rectangle(Point(1.5, 1.25), Point(2.5,1.75)).draw(win).setWidth(4)

#Wait for mouse click
win.getMouse()

#Converting all inputs from the pre mouse click into integers to be used in total price calculations
bagel1 = int(inputBagel1.getText())
cheese1 = int(inputCheese1.getText())
butter1 = int(inputButter1.getText())
bagel2 = int(inputBagel2.getText())
cheese2 = int(inputCheese2.getText())
butter2 = int(inputButter2.getText())
bagel3 = int(inputBagel3.getText())
cheese3 = int(inputCheese3.getText())
butter3 = int(inputButter3.getText())
regular = int(inputCoffee1.getText())
decaf = int(inputCoffee2.getText())

#Use inputs in calculations
priceBagel1 = (bagel1 * 1.75)
priceBagel2 = (bagel2 * 1.75)
priceBagel3 = (bagel3 * 1.75)
priceCreamCheese1 = (cheese1 * .5)
priceCreamCheese2 = (cheese2 * .5)
priceCreamCheese3 = (cheese3 * .5)
priceButter1 = (butter1 * .25)
priceButter2 = (butter2 * .25)
priceButter3 = (butter3 * .25)
priceRegular = (regular * 1.95)
priceDecaf = (decaf * 1.85)
#This long thing just adds everything up
totalPrice = (priceBagel1 + priceBagel2 + priceBagel3 + priceCreamCheese1 + priceCreamCheese2 + priceCreamCheese3 + priceButter1 + priceButter2 + priceButter3 + priceRegular + priceDecaf)
priceTaxed = (totalPrice * 1.07)

#Writing
sentence1 = Text(Point(2,.5), 5)
sentence1.setText("Your total price before tax")
sentence1.draw(win)
sentence2 = Text(Point(2,.4), 5)
sentence2.setText("Your total price after tax")
sentence2.draw(win)

#Total output box's
pricepreTax = Text(Point(3,.5), 5)
pricepreTax.setText(totalPrice)
pricepreTax.draw(win)
pricepostTax = Text(Point(3,.4), 5)
pricepostTax.setText(priceTaxed)
pricepostTax.draw(win)

#Change button
button.setText('Quit')

#Bagel Drawing
circle1 = Circle(Point(1,.5), .4)
circle1.setFill('brown')
circle1.draw(win)
circle2 = Circle(Point(1,.5), .17)
circle2.setFill('white')
circle2.draw(win)

#Wait for click and then quit
win.getMouse()
win.close()
