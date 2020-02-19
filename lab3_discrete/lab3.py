'''
Ethan Shealey, Vincent Fazio, Tia Carlson, Greyson Richart
CSC-2342-01
02/14/2020

Finding onto and one-to-one functions based on user inputted sets
'''
from random import seed, randint

# Seed random
seed()

_quit = False

# Function to print out the mapping
def print_function(setA, setB):
    # Loop through and create the function
    print('f: ', end='')
    for i in range(len(setA)):
        if i < len(setB):
            print(setA[i], '→', setB[i], end = ', ' if i != len(setA) - 1 else '\n')
        else:
            print(setA[i], '→', setB[randint(0, len(setB)-1)], end = ', ' if i != len(setA) - 1 else '\n')

print('Input Example: Apple, Goat, Boot, Knee')
while not _quit:

    # Get user input
    setA = list(set(input('Input set A: ').split(', ')))
    setB = list(set(input('Input set B: ').split(', ')))
    choice = input('One-to-one or Onto?: ').lower()

    # Invalid one-to-one
    if len(setA) != len(setB) and choice == 'one-to-one':
        print(setA, 'and', setB, 'cannot be one-to-one')

    # Invalid onto
    elif len(setA) < len(setB) and choice == 'onto':
        print(setA, 'and', setB, 'cannot be onto')
        
    # Both one-to-one and onto
    elif len(setA) == len(setB):
        if choice == 'onto':
            print('This function can only be one-to-one and onto')
        print_function(setA, setB)

    # Valid Onto
    elif len(setA) > len(setB) and choice == 'onto':
        print_function(setA, setB)

    if input('Continue or Quit?\n').lower() == 'quit':
        _quit = True