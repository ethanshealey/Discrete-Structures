'''
Ethan Shealey, Vincent Fazio, Tia Carlson
CSC-2342
2/17/2020
'''
from math import floor, ceil
from random import seed, randint
# Get Input
a = input('Enter a: ')
# Seed random
seed()
# Get random number
random = randint(1, int(a))
# Print formula
print('%s = %i(%i) + %i' % (a, floor(int(a)/random), random, (ceil(random*((int(a)/random) - floor(int(a)/random)))) if int(a) % 2 != 0 else (floor(random*((int(a)/random) - floor(int(a)/random))))))

