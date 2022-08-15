"Challenge 13 - Curso Python #07"
#Make an algorithm that reads an employee is salary
#and displays their new salary, with a 15% increase.

INCREASE_PERCENTAGE = 15/100
FirstSalary = float(input('Enter your current salary amount: US$'))
print(f'Your current salary is US${FirstSalary:.2f}, \
and you got {INCREASE_PERCENTAGE*100:.2f}% raise.\n \
You new salary with increase is US$ {FirstSalary+(FirstSalary*(INCREASE_PERCENTAGE)):.2f}')
