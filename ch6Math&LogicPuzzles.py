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


"""