""" 6.1 The Heavy Pill


Question:

    You have 20 bottles of pills. 19 bottles have 1.0 g pills, but one contains
    1.1g pills. Given a scale that provides an exact measurement, how would you
    find the heavy bottle? You may only use the scale once.

---


The trick is in taking the pills from the bottle in ordered fashion. This
essentially marks the pills where they have came from.

For example, let us take a single pill from a bottle #1. Two pills from bottle
#2...through #20. Suppose that all the pills were in their correct weight, then
we have following:

    (1 + 2 + 3 + ... + 19 + 20) = 20(21) / 2 = 210 grams

But because we have taken varying amount of pills from each of the bottle, the
slight difference will mark the # of bottle as where it would have come from.
For example, suppose that bottle #4 contains the heavy pills. Then, the overall
weight would have been increased by 0.4 grams. Thus, this effectively allows us
to find the where the pill has come from.

"""
