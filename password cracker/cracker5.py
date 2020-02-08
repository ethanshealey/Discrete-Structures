'''
Ethan Shealey
CSC-3810

A simple dictionary attack program
'''
import hashlib
import time

begin = time.time()

with open('words.txt', 'r') as file:
    hashed_words = [hashlib.sha256(w.rstrip().encode()).hexdigest() for w in file]

with open('hashes.txt', 'r') as file:
    hashes = [h.rstrip() for h in file]

matches = set(hashed_words) & set(hashes)

hw = ['Match Found!' if i in matches else 'Match Not Found!' for i in hashed_words]

print(hw)

end = time.time()-begin

print('Total Time: {}'.format(end))
