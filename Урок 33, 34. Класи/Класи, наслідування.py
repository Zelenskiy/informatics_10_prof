class Animals():
    name = ''   
    age = ''    
    countLegs = 0     
    
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
       
    def sayName(self):
        print(self.name)
    

class Cat(Animals):
    color = '' 
    breed = '' 
    
    def say(self):
        print ("Мяу")


class Dog(Animals):
    color = '' #колір
    breed = '' #порода
    def say(self):
        print ("Гав")
    

dog_1 = Dog()
dog_1.name = 'Барсік'
dog_1.age = 5
dog_1.color = 'Чорний'
dog_1.breed = 'бульдог'

print ("У мене є собака. Її звати",dog_1.name)
print ("Їй",dog_1.age, "років")
dog_1.say()
print ()
cat = Cat()
cat.name = "Рижик"
cat.family = "котові"
cat.countLegs = 4
print ("У мене є кіт. Його звати",cat.name)
cat.say()


       

pet_1 = Cat(name="Рижик", age=5)
pet_1.name = 'Рижик'
pet_1.age = 5
pet_1.clas = 'ссавці'
pet_1.family = 'котові'
pet_1.tip = 'хордові'
pet_1.порода = 'кіт звичайний'
pet_1.number = 'хижі'
pet_1.color = 'рудий'

print (pet_1.age)
pet_1.say()
pet_1.sayName()



    
        
