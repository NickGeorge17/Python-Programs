class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myname(self):
    print("Hello my name is", self.name)

  def myage(self):
    print("I am", self.age, 'years old.')

class God(Person):
    def agegod(self):
        print('I am a god! I am', self.age, 'years old.')
    

p1 = Person("Rebecca", 21)
p2 = Person('Nick', 20)
g1 = God('Loki', 10689)
g2 = God('Thor', 10690)

p1.myname()
p1.myage()
p2.myname()
p2.myage()

g1.myname()
g1.agegod()
g2.myname()
g2.agegod()
#I took this from w3 schools because mine kept breaking and was too complex for me to figure out correctly
#https://www.w3schools.com/python/python_classes.asp
