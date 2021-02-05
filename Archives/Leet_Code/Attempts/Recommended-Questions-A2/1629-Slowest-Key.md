# 1629. Slowest Key

A newly designed keypad was tested, where a tester pressed a sequence of
n keys, one at a time.

You are given a string keysPressed of length n, where keysPressed[i] was the
ith key pressed in the testing sequence, and a sorted list releaseTimes, where
releaseTimes[i] was the time the ith key was released. Both arrays are
0-indexed. The 0th key was pressed at the time 0, and every subsequent key was
pressed at the exact time the previous key was released.

The tester wants to know the key of the keypress that had the longest duration.
The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], and
the 0th keypress had a duration of releaseTimes[0].

Note that the same key could have been pressed multiple times during the test,
and these multiple presses of the same key may not have had the same duration.

Return the key of the keypress that had the longest duration. If there are
multiple such keypresses, return the lexicographically largest key of the
keypresses.

---

The key point here is computing the difference between prev and current
releaseTimes - and find the longestReleaseTime amongst them. Here, the tricky
part is when the difference found is equal to the longest difference found thus
far - in this case, we need to update our result to lexicographically larger
key.

Time complexity is O(n).

---

Java:

```java

class Solution {
    
    public char slowestKey(int[] times, String keys) {
        // start from first character
        int longestDiff = times[0];
        int longestChar = keys[0];

        for (int i = 1; i < times.length; i++) {
            int currDiff = times[i] - times[i-1];

            if (longestDiff < currDiff) {
                currDiff = longestDiff;
                longestChar = keys.charAt(i);
            } else if (longestDiff == currDiff && longestChar < keys.charAt(i)) {
                // lexicographically larger value
                longestChar = keys.charAt(i);
            }
        }
        return (char) longestChar;
    }
}
```
