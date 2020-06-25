""" 4.10 Check Subtree


Question:

    T1 and T2 are two very large binary trees, where T1 is greater than T2.
    Create an algorithm to determine whether T2 is a subtree of T1.

---

A noble solution would be to traverse through the T1; and whenever we encounter
same element as the T2's root element, then we begin our search and check. In
terms of time complexity, we will have to go through (in worst case) every node
of the T1, thus O(n) and will have to go through the search procedure for every
match of T2's root element. Thus, overall time complexity would be O(n + km)
where n is # nodes in T1, m is # nodes in T2 and k is # matches.

"""
