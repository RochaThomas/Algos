# cracking the coding interview
# chapter 7 object oriented design

# interview questions

"""
7.1 deck of cards
design the data structures of a generic deck of cards. explain how you would subclass the data structure to implement
blackjack

for a 52 deck of cards

suit class
    takes in value and records a suit based on value

deck class
    has an array of 52 cards
    keeps track of an index for the place in the deck
    methods for shuffling and getting the number of remaining cards in the deck

card class
    has a value 1-13
    has a suit
    has a boolean to indicate whether or not it is available

hand class
    has an array of cards
    has a score 
    methods for adding and removing cards
"""

"""
7.2 call center
imagine you have a class center with 3 levels of employees, respondent, manager, and director
incoming calls are directed to a free responder
that call can be redirected to manager
if the manager isn't free then it goes to the director
design classes and data structures for this problem
implement a method dispatchCall() which assigns a call to the first available employee


"""