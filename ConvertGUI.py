#convert_gui.py
#Program to convert Celsius to Fahrenheit using a simple graphical interface
from graphics import *

win = GraphWin('Celsius Converter', 450, 400)
win.setCoords(0.0, 0.0, 4.0, 4.0)

#Draw Interface
Text(Point(1.5,3), ' Celsius Temperature:').draw(win)
Text(Point(1.5,1), 'Fahrenheit Temperature').draw(win)
inputCelcius = Entry(Point(2.8,3), 5)
inputCelcius.setText('0.0')
inputCelcius.draw(win)
outputCelsius = Text(Point(2.8,1), 5)
outputCelsius.draw(win)
button = Text(Point(2,2.0), 'Convert It')
button.draw(win)
Rectangle(Point(1.5, 1.5), Point(2.5,2.5)).draw(win)

#Wait for mouse click
win.getMouse()

#Convert input
celsius = float(inputCelcius.getText())
fahrenheit = 9.0/5.0 * celsius + 32

#Display output and Change button
outputCelsius.setText(round(fahrenheit,2))
button.setText('Quit')

#Wait for click and then quit
win.getMouse()
win.close()
