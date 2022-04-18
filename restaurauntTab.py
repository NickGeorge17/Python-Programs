tax = float(input('enter tax%: '))

certificate = float(input("enter amount of gift certificate: "))
print('enter ordered items for person 1')
appetizerPer1 = float(input('appetizer: '))
entreePer1 = float(input('entree: '))
drinksPer1 = float(input('drinks: '))
dessertPer1 = float(input('dessert: '))

print('\nenter ordered items for person 2')
appetizerPer2 = float(input('appetizer: '))
entreePer2 = float(input('entree: '))
drinksPer2 = float(input('drinks: '))
dessertPer2 = float(input('dessert: '))

amtPerson1 = appetizerPer1 + entreePer1 + drinksPer1 + dessertPer1
amtPerson2 = appetizerPer2 + entreePer2 + drinksPer2 +dessertPer2
                          
itemsCost = amtPerson1 + amtPerson2
tab = itemsCost + (itemsCost * tax)


print('Ordered Items: ${0:5.2f}'.format(itemsCost))
print('restaurant Tax: ${0:5.2f}'.format(itemsCost * tax))
print('tab: ${0:5.2f}'.format(tab - certificate))
print('(negative amount indicates unused amount of gift certificate)')
