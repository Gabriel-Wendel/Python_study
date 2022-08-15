"Challenge 10 - Curso Python #07"
#Create a program that reads how much money a person has in
#their wallet and shows how many dollars they can buy.
#Consider US$ 1.00 = R$ 3.27

CURRENT_DOLLAR_QUOTE_BRL = 3.27
firstValue = float(input('Put your value in R$: '))
print(f'The current dollar exchange rate is: {CURRENT_DOLLAR_QUOTE_BRL}\n \
Your entered value was R$ {firstValue:.2f} reais and \n \
its value converted to dollar is US${(firstValue/CURRENT_DOLLAR_QUOTE_BRL):.2f} dollars.')
