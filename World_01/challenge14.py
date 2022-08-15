"Challenge 14 - Exercício Python #14"
# Write a program that converts a temperature
# typed in C°(Celsius) to F°(Fahrenheit).

temperatureValue = float(
    input('Enter the temperature value to be converted: '))
convertTo = input('Enter what temperature you want to convert to \n \
1 for Celius or \
2 for Fahrenheit')
C_TO_F_FORMULA = (temperatureValue * 9/5) + 32
F_TO_C_FORMULA = (temperatureValue - 32) * 5/9
if convertTo == '1' or convertTo == '2':
    if convertTo == '1':
        print(f'The entered temperature was {temperatureValue:.2f} C \
and converted is {C_TO_F_FORMULA:.2f} F')  
    if convertTo == '2':
        print(f'The entered temperature was {temperatureValue:.2f} F \
and converted is {F_TO_C_FORMULA:.2f} C')
else:
    print('You entered an invalid option')