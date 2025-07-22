def calSquare(x):
    print(x**2)


calSquare(9)

def addNum(num1,num2):
    return num1+num2

print(addNum(9995,6777))



def returnMultipleValues(radius):
    import math
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    return (area,circumference)

a,c=returnMultipleValues(5)
print(f"area is {a} and circumference is {c}")


def greetUser(name="user"):
    print(f"hellow {name}")

greetUser("hamza")


cube=lambda x:x**3

print(cube(5))


def sumAll(*args):
    for i in args:
        print(i)
    return sum(args)

print(sumAll(1,2,3,4,5,6,7))

def kwArgs(**kargs):

    for key,value in kargs.items():
        print(key,value)

kwArgs(name="ali",hamza="hamza",marks=234)


# def returnListOfEven(upTo):
#     li=[]
#     for i in range(2,upTo+1,2):
#         li.append(i)
    
#     return li

# for i in returnListOfEven(20):
#     print(i)
def returnListOfEven(upTo):
   
    for i in range(2,upTo+1,2):
       yield i
    
   

for i in returnListOfEven(20):
    print(i)


def calculateFactorial(num):
    
    if num==0:
        return 1
    
    else:

        return num*calculateFactorial(num-1)


# print(calculateFactorial(800))

username="ali"

def funcOne():
    username="hamza"

funcOne()
print(username)    
