# 75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively.

---

There are three colors or integers to sort out. Hence, we will use one of them
as a default value to insert. As we iterate and checking for the values, if the
value was not the default value, we insert next color; if it wasn't that
either, then next. This is done so with each pointers where they have been
inserted last.

---

Python:

```python

class Solution75:

    def sortColors(self, nums):

        # red = 0, white = 1, blue = 2
        redIns, whiteIns = 0, 0

        for i in range(len(nums)):
            currColor = nums[i]

            # insert blue by default
            nums[i] = 2

            # check whether current color was indeed blue
            # if it was not, insert white first
            if currColor < 2:
                nums[whiteIns] = 1
                whiteIns += 1
            
            # if it was red, then insert red
            if currColor == 0:
                nums[redIns] = 0
                redIns += 1
```
