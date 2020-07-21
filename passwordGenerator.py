import random
import string

LETTER = string.ascii_letters
NUMBERS = '0123456789'
SPECIAL = '+-*@#$%&'
SYMBOL = LETTER + NUMBERS + SPECIAL
length = int(input('Enter the length: '))
password = ''.join(random.sample(SYMBOL, length))
print(password)
