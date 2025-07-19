from first import printSomething

printSomething("nothing just for fun")

import os

print(os.getcwd())

from importlib import reload
import second

print(second.varOne)
print(second.varThree)
reload(second)
print(2*6)