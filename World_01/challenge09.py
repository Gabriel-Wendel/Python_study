"Challenge 05 - Curso Python #07"
#Write a program that reads any integer
#and displays its multiplication table on the screen.

firstNumber = int(input('Enter an integer: '))
print(f'{"-" * 4} Multiplication Table {"-" * 4}')
TABLENUMBER = 1
X = 0
while X < 10:
    print(f'{firstNumber} x {TABLENUMBER:3} = {(firstNumber)*(TABLENUMBER)}\n')
    X = X + 1
    TABLENUMBER = TABLENUMBER + 1
print(f'{"-" * 30}')
