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

call handler class
    has num of employee levels
    has num of employess at each level
    has list of employee levels corresponding to index
    has array of employees
    has a queue of calls

    has a method getHandlerForCall which gets the first available employee who can handle the call
    has method dispatchCall which routes the call to an employee or saves in queue if none are available
        calls getHandlerForCall that gets employee of minimal rank to handle call
            if employee available then set handler for call to that employee
            else call goes into the queue
    
call class
    has rank of employee who can handle the call
    has caller
    has handler
    methods for reply, increment rank, and disconnect

employee class
    has currentCall
    has rank
    methods for receiveCall, callCompleted, escalateAndReassign, assignNewCall, isFree

director class
    extends employee and rank is director
manager class
    extends employee and rank is manager
respondent class
    extends employee and rank is respondent
"""

"""
7.3 jukebox
design a musical jukebox using object-oriented principles

jukebox class
    has array of songs
    has price
    has queue of songs
    has currentTotal
    has currentSong
    methods play, playNext, addSong, removeSong

user class
    has song
    has money
"""

"""
7.4 parking lot
design a parking lot using object-oriented principles

parking lot class
    has array of spots
    method needs spot
        takes in car
        finds free spot
        sets spot car
        sets car needsSpot
    method carLeft

spots class
    has car

car class
    had needsSpot
"""

"""
7.5 online-book reader
design data structures for an online book reader system

online reader system class
    has library, userManager, and display
    methods getActiveBook, setActiveBook, getActiveUser, getActiveUser

library class
    has hashmap of books
    methods addBook, remove book, findBook

user manager class
    has hashmap of books
    methods addUser, find, and remove

display class
    has activeBook, activeUser, and pageNumber
    methods displayUser, displayBook, turnPageForward, turnPageBackward

book class
    has bookId and details
user class
    has userId, details, and accountType
"""

"""
7.6 jigsaw
implement an NxN jigsaw puzzle. design the data structures and explain an algorithm to solve the puzzle. Assume there
is a fitsWith method that returns true for two pieces if the two edges fit together

wayyy too confusing. revisit this solution in the book
"""

"""
7.7 chat server
explain how you would design a chat server. provided details about the various backend components, classes, and methods.
what would be the hardest problem to solve?

also too complex to note here. take a look at the indepth solutionn on page 323
"""

"""
7.8 othello
othello is played by placing tiles one by one. if a piece is surrounded on top and bottom or left and right by the opposite 
color then flip the tile. game ends when there are no other moves to be made. winner is who evers color shows more

robust solution page 326
remember, often times what you did is not important, its more important WHY you did what you did. 
during interviews always discuss why you are doing something and what the tradeoffs are for that method as opposed to another
"""

"""
7.9 circular array
implement a circular array class that supports an array-like data structure which can be efficiently rotated
should support iteration

see book pg 329
"""