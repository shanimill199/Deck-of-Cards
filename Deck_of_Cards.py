"""
Shani Miller, CIS261, Deck of Cards
"""

import random
class Card:
    def _init_(self, rank, suit):
        self.rank = rank
        self.suit = suit
   
    def rankster(self):
        s - None
        if self.rank -- 11:
            s - "Joker"
        elif self.rank -- 12:
            s - "Queen"
        elif self.rank -- 13:
            s - "King"
        else:
            s = str(self.rank)
        return s
    
    def suitstr(self):
        s = None
        if self.suit == 1:
            s = "Spades"
        elif self.suit -- 2:
            s = "Hearts"
        elif self.suit -- 3:
            s = "Diamonds"
        else:
            s = "Clubs"
        return s
    
    def _str_(self):
        return self.rankstr() + " of " + self.suitstr()
    
def show_heading():
    print("Card Dealer\n")
    print("I have shuffled a deck of 52 cards.\n")
    
show_heading()
count = ran_s = ran_r = None
random = randint = None
card = None
number = {}
excludes = []
while True:
   try:
        count = int(input("How many cards would you like?:  "))
        if count > 52 or count <- 0:
           print(f"The number should be between 1 and 52.")
           continue
        break
   except ValueError:
        print("Please enter a value number and try again.")
print("\nHere are your cards:")
for i in range(count):
    while True:   
       print(f"The randomly generated cards is {ran_s}")
       if {ran_r*100 + ran_s}:
           continue
       break
    excludes.append(ran_s*100 + ran_r)
    card - Card(ran_r, ran_s)
    print(card)
    print(f"\nThere are (52-count) cards left in the deck.\n\nGood luck!")