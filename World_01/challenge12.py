"Challenge 12 - Curso Python #07"
#Make an algorithm that reads the price of a product
#and displays its new price, with a 5% discount

DISCOUNT_PERCENTAGE = 5/100
firstPrice = float(input('Enter the product price: US$'))
print(f'The value of your product is US${firstPrice:.2f}, \
and you have a {DISCOUNT_PERCENTAGE*100:.2f}% discount.\n \
The new discounted product value will be US$ {firstPrice-(firstPrice*(DISCOUNT_PERCENTAGE)):.2f}')
