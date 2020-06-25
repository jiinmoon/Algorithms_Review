""" 6.4 Ants on a Triangle


Question:

    There are three ants on a different verticies of a triagle. What is the
    probability of collision between any two or all of them is they start
    walking on the sides of the triagle? Assume that each any randomly picks a
    direction, with either direction being equally likely to be chosen, and tha
    tthey walk at the same spped.

    Similarly, generalize for any n-vertex polygon.

---

The probability of collision would be 1 - the probability of not colliding.
Thus, we are looking for probability that the all the ants have chosen to move
in clockwise or anti-clockwise fashion. Since at each vertex, the ant has 50/50
to move in either direction, if this was a triangle...

P(ants moving in clockwise fashion)
    = (1/2) ^ 3 # 50% chance to move / three verticies

P(ants moving in counter-clockwise fashion)
    = (1/2) ^ 3

Thus, chance of colliding must be...

P(collide)
    = 1 - P(not colliding)
    = 1 - 2((1/2)^3))
    = 1/4

Thus, the probability that the ants will collide will be 25%.

To generalize, we substitute number of verticies with n for where n is the
number of verticies within the n-polygon.


"""
