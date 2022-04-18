from graphics import *

win = GraphWin('School Tax thing', 450, 400)
win.setCoords(0.0, 0.0, 4.0, 4.0)

#Draw Interface
Text(Point(1.5,3), ' House Value:').draw(win)
Text(Point(1.5,2.5), 'Tax:').draw(win)
Text(Point(1.5,0.5), 'School Tax:').draw(win)

#inputHouse Value
inputHouse = Entry(Point(2.8,3.0), 5)
inputHouse.setText('0.0')
inputHouse.draw(win)

#School Tax output box
schoolTax = Text(Point(3,.5), 5)
schoolTax.setText('0.0')
schoolTax.draw(win)

#Tax output box for if statement
taxBox = Text(Point(2.5,2.5), 5)
taxBox.setText('0.0')
taxBox.draw(win)

#Add tax button & rectangle
button = Text(Point(2,1.5), 'Do ya taxes')
button.draw(win)
Rectangle(Point(1.5, 1.0), Point(2.5,2.0)).draw(win)

#Wait for mouse click
win.getMouse()

#have to convert house val to a float sooner than later
houseVal = float(inputHouse.getText())

#if or statement
if houseVal < 300000 :
    tax = (.98)
    taxBox.setText('%98')

if houseVal > 300000 :
    tax = (.985)
    taxBox.setText('%98.5')

#School taxes output
schoolTax.setText((tax * houseVal))
button.setText('Beat it, buster')

#Wait for click and then quit
win.getMouse()
win.close()
