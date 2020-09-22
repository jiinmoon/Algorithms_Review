621 Task Scheduler
==================

Given a characters array _tasks_ that represents tasks that CPU needs to
process where each character represents a different tasks. Tasks can be
completed in any order.

There is non-negative integer `n` that represents the cooldown period between
two same tasks - there must be at least n units of time between any two same
tasks.

Return the least number of units of times that the CPU will take to finish all
the given tasks.

---

Note that if there are not enough tasks, then CPU can go into _idle_. For
example,

```
[A,A,A,B,B,B] and n = 2

A -> B -> idle -> A -> B -> idle -> A -> B
```

Since we can fill the gaps with the idle time, the time that will be required
to complete all the task is determined by most frequently appearing task or
_tasks_. The time to complete this most frequently appearing task depends on
the wait time `n`. To be precise, `n+1` indicates the wait time between the
tasks (number of tasks or idle appearing between the most frequent task). And
number of times that we need to wait is determined by the number of frequent
task - 1.

However, since there can be multiple of same most frequently appearing tasks,
each will push back the least number of units of time that the CPU will take to
finish.

Notice that this is possible due to idle time - since all other less frequently
appearing tasks can be scheduled to take place instead of the idle time.
However, if they cannot, then it extends the finish time.

---

```python
class Solution:
    def taskScheduler(self, tasks, N):
        taskCounter = collections.Counter(tasks)
        mostFreqTask = max(taskCounter.values())
        
        # finish_time = number_of_waits * wait_time (# idles)
        maxTime = (mostFreqTask - 1) * (N + 1)
        
        # extend maxTime for same frequent tasks
        for freqTask in taskCounter.values():
            if freqTask == mostFreqTask:
                maxTime += 1

        # remaining tasks can fill idle gaps;
        # or it extends further
        return max(result, len(tasks))
```

