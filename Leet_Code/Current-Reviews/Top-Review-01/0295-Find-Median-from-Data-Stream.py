# 295 Find Median from Data Stream
#
# To find the median in the stream, the simplest method would be to maintain
# two queues where their elements are balaned. This is achieved with using max
# and min heaps.
#
# We maintain one heap 1 more than other in case of odd.

import heapq

class MedianFinder:
    def __init__(self):
        self.l = list() # max heap
        self.r = list() # min heap

    def addNum(self, num):
        heappush(self.l, -num)
        heappush(self.r, -heappop(self.l))
        if len(self.l) > len(self.r):
            heappush(self.l, -heappop(self.r))

    def median(self):
        if len(self.l) > len(self.r):
            return self.l[0]
        return (self.l[0] + self.r[0]) * 0.5
