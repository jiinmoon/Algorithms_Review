# 529. Random Pick with Weight

You are given an array of positive integers w where w[i] describes the weight
of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in
the range [0, w.length - 1]. pickIndex() should return the integer proportional
to its weight in the w array. For example, for w = [1, 3], the probability of
picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of
picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

---

First, create a weighted number line - that is a cumulative weights. Then, we
can randomly select the value from 1 to last cumulative weights and use binary
search algorithm to find the index of the chosen value. The time complexity
should be O(n) for construction and O(log(n)) for choosing random index.

---

Java:

```java

class Solution {

    private int[] weights;

    public Solution(int[] w) {
        this.weights = new int[w.length];
        int temp = 0;
        for (int i = 0; i < w.length; i++) {
            temp += w[i];
            this.weights[i] = temp;
        }
    }

    public int pickIndex() {
        int target = (int) Math.random() * this.weights[this.weights-1] + 1;
        return binarySearchLeft(target);
    }
    
    // find left most occurrence of target or would be insert position
    private int binarySearchLeft(int target) {
        int l = 0;
        int r = this.weights.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (this.weights[mid] > target) l = mid + 1;
            else r = mid;
        }
        return l;
    }
}

```

Python:

```python

class RandomPick:
    def __init__(self, weights):
        self.weights = list()
        temp = 0
        for weight in weights:
            temp += weight
            self.weights.append(temp)

    def pickIndex(self):
        i = random.randint(1, self.weights[-1])
        return bisect.bisect_left(self.weights, i)
```
