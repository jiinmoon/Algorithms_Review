""" 453. Minimum Moves to Equal Array Elements

Question:

    Given an non-emptry array, find the minimum number of moves to bring every
    element to eual another. A single move is incrementing n-1 elements by 1.

+++

Solution:

    [1, 4, 3, 2]

    The minimum number of moves have be depend upon the minimum of the array.
    Above example, we have 1 as our minimum. Let's see our progress.

    1432 - 2443 - 3454 - 4555 - 5665 - 6676 - 7777

    As we can see, to reach the equilibrium, the min value 1 had to be increased
    six times. The value that needs to be reached is the minimum number of moves
    required here. Thus, we have two options.

    First, naive approach would be to actually simulate the moves - that is to
    except the maximum, add 1 to all elements until they are equal. But this is
    tricky to implement as we have to find the maximum at each iteration as it
    can change or tie.

    The preferred option is simply realizing that to max value that the values
    can reach is the sum of each elements - the minimum value.

"""

class Solution:
    def minMovesToEqual(self, nums):
        minMoves = min(nums)
        total = sum([num - minMoves for num in nums])
        return total
