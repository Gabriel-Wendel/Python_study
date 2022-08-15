"Challenge 11 - Curso Python #07"
#Write a program that reads the width and height of a wall in meters,
#calculates its area and the amount of paint needed to paint it,
#knowing that each liter of paint paints an area of 2m²

INK_YIELD = 2
wallWidth = float(input('Enter the wall width in meters: '))
wallHeight = float(input('Enter the height of the wall in meters: '))
wallDimension = wallWidth * wallHeight

print(f'The dimension of your wall of {wallWidth:.2f}x{wallHeight:.2f} is {wallDimension:.2f}m²,\n \
and you will need {(wallDimension/INK_YIELD):.2f} liters of paint to paint it completely')
