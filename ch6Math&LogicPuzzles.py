# cracking the coding interview
# chapter 6 math and logic puzzles

# interview questions

# 6.1 the heavy pill
# you have 20 pill bottles. 19 filled with 1.0 g pills and 1 filled with 1.1 g pills.
# given a scale that provides exact measurements, how can you figure out which bottle has the heavy pills
# while only using the scale once

"""
imagine there were only two bottles, if you put 1 pill from bottle 1 and 2 pills from bottle 2.
there are two outcomes. it weighs 3.1 or 3.2. if all weighed 1.0 then it would be 3.0 so the discrepency must come from
the heavier bottle

put 1 pill from bottle 1, 2 from bottle 2, 3 from bottle 3...etc
there would be 210 pills in total, 210 grams if all weighed 1.0
if the scale reads 212.0. 212.0 - 210 -> bottle 20
if the scalre reads 210.1 -> bottle 1
211.0 -> bottle 10
etc
"""

"""
6.2 basketball
you have a ball and a hoop and can play 1 of 2 games
game 1 you get 1 shot to make the hoop
game 2 you get 3 shots to make 2/3 shots
if p is the probability of making a particular shot then for which values of p should you play game 1
and what values should you play game 2

set up an equation where the prob of game 1 given p >= prob of game 2 given p
prob of winning game 1 is just p
prob of winning game 2 is prob of making 2/3 shots + prob of making 3/3 shots
    prob of making 2/3 shots is
        prob of making 1 and 2 but not 3 +
        prob of making 1 and 3 but not 2 +
        prob of making 2 and 3 but not 1

        = p * p * (1 - p) + p * (p - 1) * p + (p - 1) * p * p
        = 3(p - 1) * p2
    prob of making 3/3 shots is
        = p * p * p = p3
    total prob
        = p3 + 3p2(1 - p) = p3 + 3p2 - 3p3 = 3p^2 - 2p^3

if prob of game 1 is higher than game 2 then play game 1
if p > 3p^2 - 2p^3
    1 > 3p - 2p2
    2p2 - 3p - 1 > 0
    (2p - 1)(p - 1) > 0
    ^ for this to be true both terms must be the same sign
    we know p must be below 1 so both must be negative
    2p - 1 < 0
    2p < 1
    p < 0.5
if p < 0.5 play game 1 if 0.5 < p < 1.0 play game 2
"""

"""
6.3 dominos
given an 8x8 chess board with opposite diagonal corners cut off and a set of 31 dominos where 1 domino can cover 2 squares
can you cover the entire board
prove it

8 x 8 = 64
64 - 2 squares = 62
31 dominos x 2 squares = 62
should work... but... its impossible

its impossible because of the corners that have been cut off
you can orient your dominos in 1 of two ways, both way result in an over hand of 1 square regardless of orientation
rotating the board doesn't change anything either

by cutting off the corners you are cutting off 2 of the same color. usually there are 32 black and 32 white but cutting off the
corners results in 30 black and 32 white or vice versa, the problem with this is that when a domino covers 2 squares it's always
going to cover 1 white and 1 black. it can never cover up 2 of the same color with 1 domino so
with 31 dominos you can only cover up 31 whites and 31 blacks, never reaching the 32 mark that is needed
"""

"""
6.4 ants on a triangle
imagine a triangle where an ant starts on each vertex. what is the probability of a collision of ants given that they all walk
at the same speed and the direction they choose to walk in is equally probable?

a collision happens if 1 ant walks in a different direction than the other two
the only way a collision doesn't happen is if all three walk in the same direction
    prob of no collision
    p(clockwise) = 1/2^3
    p(counterclockwise) = 1/2^3
    so p(same direction0 = (1/2)^3 + (1/2)^3 = 1/4
p(collision) = 1 - p(no collision)
1.00 - 0.25 = 0.75
"""

"""
6.5 jugs of water
given a 5qt jug, a 3qt jug, and an unlimited supply of water
how would you come up with exaxtly 4 qts of water?
you do not know where the half is in any jug


"""