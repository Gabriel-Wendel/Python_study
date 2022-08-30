"Practice 01 - Curso Python #08"
#Practice - Use Modules
#https://docs.python.org/3/library/index.html
#https://pypi.org/

import math
firstNumber = int(input('Enter a number: '))
root = math.sqrt(firstNumber)
print(f'The square root of {firstNumber} is {math.ceil(root)}.')

from math import sqrt,floor
firstNumber = int(input('Enter a number: '))
root = sqrt(firstNumber)
print(f'The square root of {firstNumber} is {floor(root)}.')

import random
firstNumber = random.randint(1,10)
print(firstNumber)
