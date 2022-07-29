"Challenge 04 - Curso Python #06"

firstEntry = input('Type something: ')
entryType = type(firstEntry)
print('{}, is of type {}'.format(firstEntry,entryType))
print('Just spaces? {}'.format(firstEntry.isspace()))
print('Is it numeric? {}'.format(firstEntry.isnumeric()))
print('Is it alphabetic? {}'.format(firstEntry.isalpha()))
print('Is it alphanumeric? {}'.format(firstEntry.isalnum()))
print('Is it capital only? {}'.format(firstEntry.isupper()))
print('Is it just lowercase? {}'.format(firstEntry.islower()))
print('Is it capitalized? {}'.format(firstEntry.istitle()))