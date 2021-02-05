# 846 Hand of Straights

class Solution:
    def handOfStraights(self, hand, W):
        if not hand or not W or len(hand) % W:
            return False

        counter = collections.Counter(hand)

        for currNum in sorted(hand):
            count = counter[currNum]
            if not count:
                continue

            for nextNum in range(currNum, currNum + W):
                if nextNum not in counter or counter[nextNum] < count:
                    return False
                counter[nextNum] -= count

        return True

