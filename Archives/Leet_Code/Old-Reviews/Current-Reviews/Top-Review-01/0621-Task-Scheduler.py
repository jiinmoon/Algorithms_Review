# 621 Task Scheduler
# 
# The max time that would take is determined by the number of most frequent
# task and value of N. Then, this time is increased for each other task with
# same frequency.

class Solution:
    def taskScheduler(self, tasks, n):
        counter = collections.Counter(tasks)
        maxTask = max(counter.values())
        maxTime = (maxTime - 1) * (n + 1)

        for count in counter.values():
            if count == maxTask:
                maxTime += 1

        return max(maxTime, len(tasks))
