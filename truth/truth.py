'''
Ethan Shealey, Vincent Fazio, Tia Carlson, Greyson 

CSC-2342
1/30/2020
Program that generates a truth table based
on user input
NOTE: DOES NOT WORK PROPERLY WITH PARENTHESES
      Program properly parses out parantheses
      but I could not figure out how to 
      properly implement the logic into my
      program
'''
from itertools import product

class rules():

    def _and(self, left, right):
        return left and right
    def _or(self, left, right):
        return left or right
    def _imply(self, left, right):
        return not left or right
    def rules(self):
        print('/\\ - and\n\/ - or\n> - implication')

t = rules()

# Get expression
expression = input('Please enter an expression\n(i.e: a /\ b \/ ~c)\n')

if expression.lower() == 'rules':
    t.rules()
    exit()

# Split into array
expression = expression.lower().split(' ')

# Initialize variables and arrays
variables = []
operators = []

# Find the variables and operations
for i in expression:
    if i.isalpha() or i[0] is '~' and i[-1:] is not ')':
        variables.append(i)
    elif i[0] is '(':
        variables.append(i[1:])
    elif i[-1:] is ')':
        variables.append(i[:-1])
    else:
        operators.append(i)

# Create blank header
header = ''

# Create the header
if len(variables) > 1:
    for i in variables:
        header += '%-5s | ' % i
    header += ' '.join(expression)
else:
    header += '%-5s  ' % i

print(header)

# For loop that creates the truth table base values
for p in product((True, False), repeat=len(variables)):

    # Reset line and storage
    line = ''
    storage = []

    # Create row
    for x in range(len(variables)):
        if variables[x][0] is '~':
            line += '%-5s | ' % ('T' if not p[x] else 'F')
            storage.append(not p[x])
        else:
            line += '%-5s | ' % ('T' if p[x] else 'F')
            storage.append(p[x])

    if len(variables) > 1:
        # Calculate the truth for the expression
        truth = storage[0]
        for x in range(len(operators)):
            if operators[x] == '/\\':
                truth = t._and(truth, storage[x+1])
            elif operators[x] == '\/':
                truth = t._or(truth, storage[x+1])
            elif operators[x] == '>':
                truth = t._imply(truth, storage[x+1])
    
        # Attach to end of the line
        line += '%-5s' % 'T' if truth else 'F'

    print(line)