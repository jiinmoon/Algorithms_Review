# LeetCode Daily Challenge: August Week.1 - Day.2

## Question

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include following functions:

    add(value)
    remove(value)
    contains(value)

## Solution

Go:

```go
type HashSet struct {
    hashSet map[int]bool
}

func Constructor() HashSet {
    return HashSet{ map[int]bool{} }
}

func (this *HashSet) Add(key int) {
    this.hashSet[key] = true
}

func (this *HashSet) Remove(key int) {
    delete(this.hashSet, key)
}

func (this *HashSet) Contains(key int) {
    _, ok := this.hashSet(key)
    return ok
}
```

