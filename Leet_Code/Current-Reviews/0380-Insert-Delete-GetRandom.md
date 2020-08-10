380 Insert Delete GetRandom O(1)
================================

Design a data structure that supports all following operations in average O(1)
time.

 
```
 insert(val): Inserts an item val to the set if not already present.
 remove(val): Removes an item val from the set if present.
 getRandom: Returns a random element from current set of elements (it's
 guaranteed that at least one element exists when this method is called). Each
 element must have the same probability of being returned.
```

  Example:

```
  // Init an empty set.
  RandomizedSet randomSet = new RandomizedSet();

  // Inserts 1 to the set. Returns true as 1 was inserted successfully.
  randomSet.insert(1);

  // Returns false as 2 does not exist in the set.
  randomSet.remove(2);

  // Inserts 2 to the set, returns true. Set now contains [1,2].
  randomSet.insert(2);

  // getRandom should return either 1 or 2 randomly.
  randomSet.getRandom();

  // Removes 1 from the set, returns true. Set now contains [2].
  randomSet.remove(1);

  // 2 was already in the set, so return false.
  randomSet.insert(2);

  // Since 2 is the only number in the set, getRandom always return 2.
  randomSet.getRandom();
```

---

To support these operations in O(1) time, we can think of few good candidates
for our underlying datastructure such as hashmap or list.

Hashmap allows us to insert and remove at constant time, but randomizing
becomes problem since we cannot index the hashmap; we need to collect keys.
Thus, one approach would be to maintain a list of keys for the map separately.

Problem is deletion when we do it so, how do we delete key? To do this, we will
use hashmap to store the list index as its value for each element.

For insertion, we append to the list as well as add to the hashmap.

For remove, we swap the removed element with the LAST element from the list
- updating the haspmap accordingly as well, fixing the new index to currently
  removed element's index in the list.

---

Go:

```go
import (
    "time"
    "math/rand"
)

type RandomizedSet struct {
    List []int
    Map map[int]int
}


/** Initialize your data structure here. */
func Constructor() RandomizedSet {
    return RandomizedSet{[]int{}, map[int]int{}}
}


/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
    if _, ok := this.Map[val]; ok {
        return false
    }
    this.Map[val] = len(this.List)
    this.List = append(this.List, val)
    return true
}


/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
    if i, ok := this.Map[val]; ok {
        last := this.List[len(this.List)-1]
        this.List[i], this.Map[last] = last, i
        this.List = this.List[:len(this.List)-1]
        delete(this.Map, val)
        return true
    }
    return false
}


/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
    rand.Seed(time.Now().UnixNano())
    return this.List[rand.Intn(len(this.List))]
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
```

Python:

```python
from random import choice

class RandomizedSet:
    def __init__(self):
        self.l = list()
        self.d = dict()
        
    def insert(self, val: int) -> bool:
        # we do not update the lst
        # return false if key already present
        if val in self.d:
            return False
        slef.d[val] = len(self.l)
        self.l.append(val)        

    def remove(self, val: int) -> bool:
        if val in self.d:
            last, i = self.l[-1], self.d[val]
            self.l[i], self.d[last] = last, i
            self.l.pop()
            del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

