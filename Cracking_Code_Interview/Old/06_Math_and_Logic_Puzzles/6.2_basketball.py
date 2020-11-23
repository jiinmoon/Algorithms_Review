""" 6.2 Basketball


Question:

    You have a basketball hoop and someone says that you can play one of two
    games.

    Game1: You get one shot to make the hoop.
    Game2: You get three shots and you have to make two of three shots.

    If p is the probability of making a particular shot, for which values of p
    should you pick one game or the other?

---

By definition, the probability of winning game 1 is p.

The probability of winning game 2 is a bit more complex.

Let s(k, n) be the probability of making exactly k shots out of n. The
probability of winning game 2 is the probability of making exactly two shots out
of three OR making all three shots...

    P(winning) = s(2, 3) + s(3, 3)

Probability of making all three shots:

    s(3, 3) = p^3

Probability of making exactly two shots:

    P(making 1 and 2, and missing 3) +
        P(making 1 and 3, and missing 2) +
        P(making 2 and 3, and missing 1)
    = (p * p * (1 - p)) + (p * (1 - p) * p) + ((1 - p) * p * p)
    = 3(1-p)p^2

Thus, the probability of winning game 2 would be:

    s(2, 3) + s(3, 3)
        = p^3 + 3(1-p)p^2
        = p^3 + 3p^2 - 3p^3
        = 3p^2 -2p^3

Hence, we can find the whether to play game 1 or game 2 by following:

We should play game 1 if P(game 1) > P(game 2) that is

    p > 3p^2 - 2p^3
    1 > 3p - 2p^2
    2p^2 - 3p + 1 > 0
    (2p - 1)(p - 1) > 0

Thus, game 1 is prefered for p < .5; game 2 if more.

"""
