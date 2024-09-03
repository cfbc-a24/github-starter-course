import logging
logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")


import random
guess = 'foo'
while guess not in ('heads', 'tails'):
 print('Guess the coin toss! Enter heads or tails: ')
 guess = input()  #we changed it to float because it was string
 assert(guess=="heads" or guess=="tails"), "guess heads or tails, there is no alternative"
 # try asser by saying something like foo
 toss = random.randint(0, 1) # 0 is tails, 1 is heads
 if toss==1:
     toss="heads"
 else:
     toss="tails"
if toss == guess:
 print('You got it!')
else:
 print('Nope! Guess Again!')
 logging.warning("you are at the second stage of guessing")
 
 guess = input()
 if toss == guess:
     print('You got it!')
 else:
     print('Nope. You are really bad at this game.')


logging.warning("What I changed? Indentation of toss, guesss in guess, changed number input to string")
