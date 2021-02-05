# 681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by
reusing the current digits. There is no limit on how many times a digit can be
reused.

You may assume the given input string is always valid. For example, "01:34",
"12:09" are all valid. "1:34", "12:9" are all invalid.

---

Starting from left, we try to increment each digit from all the possible digits
avaialble to us - but, at each index, we have to respect the maximum value that
we can replace with. Here are general rules:

(1) if the first hour digit is '2', then second hour digit can only go upto
'3'. i.e. "23:xx".

(2) if the frist hour digit is not '2', then second hour digit goes upto '9'.
i.e. "19:xx" or "09:xx".

(3) first miniute digit can only go upto 5. i.e. "xx:5x".

(4) last minute digit can go upto "9". i.e. "xx:x9"

Hence, starting from behind, we try every possible digit that resepcts these
boundaries - if minimum digit can be found amongst them, we can replace the
time at the digit and return our new string.

Time and space both be O(1) as it is constant operation.

---

Python:

```python

class Solution681:

    def nextClosestTime(self, time):

        def findNextDigit(i):
            # max digit at each index is different

            if i == 0:
                maxDigit = 2
            elif i == 1:
                maxDIgit = 3 if time[0] == '2' else 9
            elif i == 3:
                maxDigit = 5
            elif i == 4:
                maxDigit = 9
            
            nextDigits = [d for d in digits if int(time[i]) < d <= maxDigit]
            return str(min(nextDigits)) if nextDigits else None

        result = list(time)
        digits = set(map(int, result))

        for i in range(len(result) -1, -1, -1):
            # ignore ":"
            if i == 2: continue
            nextDigit = findNextDigit(i)
            if nextDigit:
                result[i] = nextDigit
                return "".join(result)
            result[i] = str(min(digits))

        return "".join(result)
```



