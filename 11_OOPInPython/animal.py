# class Animal():
#     name="cat"
#     sound="meow"

# cat=Animal()
# print(cat.name)
# print(cat.sound)
# class Animal():
#     def __init__(self,name,sound):
#         self.name=name
#         self.sound=sound

# cat=Animal("Cat","Meow")
# print(cat.name)
# print(cat.sound)
# class Animal():
#     def __init__(self,name="animal",sound="sound"):
#         self.name=name
#         self.sound=sound

# cat=Animal()
# print(cat.name)
# print(cat.sound)
# class Animal():
#     def __init__(self,name,sound):
#         self.name=name
#         self.sound=sound
    
#     def animalInformation(self):
#         return f"animal name is {self.name} and it makes {self.sound}."

# class Cat(Animal):

#     def __init__(self,name,sound,legs):
#         super().__init__(name,sound)
#         self.legs=legs
    
#     def animalInformation(self):
#         return f"animal name is {self.name} and it makes {self.sound} and it has {self.legs}."

# cat=Animal("CAT","MEOW")
# print(cat.animalInformation())
# catTwo=Cat("CAT","MEOW" , 4)
# print(catTwo.animalInformation())

# class Animal():
#     def __init__(self,name,sound):
#         self.__name=name
#         self.__sound=sound
    
#     def get_name(self):
#         return self.__name
#     def get_sound(self):
#         return self.__sound

#     def animalInformation(self):
#         return f"animal name is {self.get_name()} and it makes {self.get_sound()}."

# class Cat(Animal):

#     def __init__(self,name,sound,legs):
#         super().__init__(name,sound)
#         self.legs=legs
    
#     def animalInformation(self):
#         return f"animal name is {self.get_name()} and it makes {self.get_sound()} and it has {self.legs}."

# cat=Animal("CAT","MEOW")
# print(cat.animalInformation())
# catTwo=Cat("CAT","MEOW" , 4)
# print(catTwo.animalInformation())
# class Animal():
#     totalAnimals=0
#     def __init__(self,name,sound):
#         self.__name=name
#         self.__sound=sound
#         Animal.totalAnimals+=1
    
#     def get_name(self):
#         return self.__name
#     def get_sound(self):
#         return self.__sound

#     def animalInformation(self):
#         return f"animal name is {self.__name} and it makes {self.__sound}."
#     @staticmethod
#     def greetAnimals():
#         print("hellow animals")
# class Cat(Animal):

#     def __init__(self,name,sound,legs):
#         super().__init__(name,sound)
#         self.__legs=legs
    
#     def animalInformation(self):
#         return f"animal name is {self.get_name()} and it makes {self.get_sound()} and it has {self.__legs}."
    
#     def getLegs(self):
#         return self.__legs

#     def guessLegs(self,userProvidedLegs):
#         if userProvidedLegs==self.__legs:
#             print("you are right")
#         else:
#             print("you are wronf")

    

# cat=Animal("CAT","MEOW")
# print(cat.animalInformation())
# catTwo=Cat("CAT","MEOW" , 4)
# print(catTwo.animalInformation())
# print(Animal.totalAnimals)
# Animal.greetAnimals()
# catTwo.guessLegs(4)
# Cat.greetAnimals()
# catTwo.__legs=34
# print(catTwo.__legs)
# print(catTwo.getLegs())


class Human:

    def __init__(self,name):
        self.__name=name
    
    def getName(self):
        return self.__name
    # @property
    # def name(self):
    #     return self.__name
    # @name.setter
    # def name(self,newName):
    #     self.__name=newName



# hamza=Human("hamza")
# # print(hamza.__name)
# hamza._Human__name="hamza two"
# # print(hamza.__name)

# # hamza.__name="new name"
# print(hamza._Human__name)
# print(hamza.getName())

# print(hamza.__dict__)
# {'_Human__name': 'hamza two', '__name': 'new name'}



# class Engine:

#     def __init__(self,engineType):
#         self.__engineType=engineType
#     @property
#     def enginType(self):
#         return self.__engineType
# class Model(Engine):

#     def __init__(self,model,year,engineType):
#         super().__init__(engineType)
#         self.__model=model
#         self.__year=year
#     @property
#     def model(self):
#         return self.__model
#     @property
#     def year(self):
#         return self.__year

# class Car(Model):

#     def __init__(self,engineType,model,year,company,country):
#         super().__init__(engineType,model,year)
#         self.__company=company
#         self.__country=country
#     def printCarInformation(self):
#         return f"Car is {self.enginType} and its model is {self.model} and production year is {self.year}. Car company is {self.__company} and origin is {self.__country}"

# teslaModelS=Car("Electric","S",2024,"Tesla","America")

# print(teslaModelS.printCarInformation())
