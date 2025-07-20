print(3+3)
print(3*3)
print(3/3)
print(3-3)
print(3**3)
print(3%3)
print(1/3.0)
print(1/4.0)
print(1==True)
print(1==False)
print(2<1)
print(2>1)
print(2==1)
print(2>=1)
print(2<=1)
print(True<2<3)

numOne=hex(34)
print(numOne)
print(bin(4))

print(int('100000',2))
print(oct(46))
print(int('46',8))
print(int('56',8))

print((1+3j)*4)
import random

print(random.random())
print(random.randint(1,10))
print(random.choice([11,22,33,44]))
list=[11,22,33,44]
random.shuffle(list)
print(list)
print({1,2,3,4}|{3,4,5,6,7})
print({1,2,3,4}&{3,4,5,6,7})
print({1,2,3,4}-{3,4,5,6,7})

from decimal import Decimal
print(Decimal('0.3')+Decimal('0.3')+Decimal('0.3')-Decimal('0.9'))