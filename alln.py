from itertools import combinations_with_replacement

characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

max_length = 4

for r in range(1, max_length+1):
    for combo in combinations_with_replacement(characters, r=r):
         if (len(combo)==4):
          print(''.join(combo))
