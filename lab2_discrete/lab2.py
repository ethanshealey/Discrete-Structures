'''
Ethan Shealey
CSC-2342

Program that does set shit
'''

from itertools import product

with open('fileA.txt', 'r') as file:
    setA = [i.split(', ') for i in file]
    setA_card = len(setA)

with open('fileB.txt', 'r') as file:
    setB = [i.split(', ') for i in file]
    setB_card = len(setB)

with open('fileC.txt', 'r') as file:
    setC = [i.split(', ') for i in file]
    setC_card = len(setC)

setA_card = len(setA[0])
setB_card = len(setB[0])
setC_card = len(setC[0])

setA = set(setA[0])
print('a:', setA)
setB = set(setB[0])
print('b:', setB)
setC = set(setC[0])
print('c:', setC)

option = input('Enter an option: ')

option = option.split(' ')

if option[0].lower() == 'a':
    first = setA
    print('setA cardinality:', setA_card)
elif option[0].lower() == 'b':
    first = setB
    print('setB cardinality:', setB_card)
elif option[0].lower() == 'c':
    first = setC
    print('setC cardinality:', setC_card)


if option[2].lower() == 'a':
    second = setA
    print('setA cardinality:', setA_card)
elif option[2].lower() == 'b':
    second = setB
    print('setB cardinality:', setB_card)
elif option[2].lower() == 'c':
    second = setC
    print('setC cardinality:', setC_card)

if option[1].lower() == 'union':
    print(first.union(second))
elif option[1].lower() == 'intersect':
    if first.intersection(second) is None:
        print(first, 'is a dijoint of', second)
    else:
        print(first.intersection(second))
elif option[1].lower() == 'product':
    productset = []
    for p in product(first, second):
        productset.append(p)
    print(set(productset))