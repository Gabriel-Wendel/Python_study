"Challenge 16 - Curso Python #08"
#Create a program that reads any real integer from the keyboard and
#displays its entire portion on the screen

from math import trunc
firstNumber = float(input('Enter a floating number: '))
print(f'The number {firstNumber} has the integer part {trunc(firstNumber)}')
