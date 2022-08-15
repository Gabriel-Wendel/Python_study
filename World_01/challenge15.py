"Challenge 15 - Exercício Python #15"
#Write a program that asks the number of Mi(Mile) traveled by a rented car 
#and the number of days for which it was rented. Calculate the price to pay, 
#knowing that the car costs US$ 60.00 per day and US$ 0.15 per mile traveled.

travaledDistance = float(input('Enter the distance traveled in miles '))
dailyUsed = int(input('Number of days used '))
DAILY_PRICE = 60.00 
MILE_VALUE = 0.15
DAILY_CALCULATION = dailyUsed * DAILY_PRICE
TRAVALED_CALCULATION = travaledDistance*MILE_VALUE
print(f'You used {dailyUsed} rental days and travaled {travaledDistance} miles. \n \
The amount of your daily spend was US${DAILY_CALCULATION:.2f}\n \
The value of your expenses with miles traveled was US${TRAVALED_CALCULATION:.2f}\n \
The total amount of your expenses was US${DAILY_CALCULATION+TRAVALED_CALCULATION:.2f}.')

