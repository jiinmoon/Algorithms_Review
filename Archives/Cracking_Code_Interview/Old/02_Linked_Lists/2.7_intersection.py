""" 2.7 Intersection

Question:

    Given two linked lists, determine if the two lists intersect. Return the
    intersecting node. NOte that the intersection is defined based on reference,
    not value/ That is, if the kth node of the first linked list is the exact
    same node as the jth node of the second linked list, then they are
    intersecting.

---

Visually, this is asking whether the two lists are ultimately one list at the
end (list medusa with multiple heads).

In order to detect the intersection, we can solve this problem by using a famous
Cycle detection algorithm - Turtle and Hare.

This is done as follows: we set up two runners that which runs at different
speed at each starting point.
"""

