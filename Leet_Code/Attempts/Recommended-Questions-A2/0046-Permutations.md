# 46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

---

To find all permutations, we are considering every possible combinations of the
given number. Using recursion, at each depth, we swap each element at current
index position to generate new permutations. Alternatively, we can reduce our
candidates one by one as we are adding them to our path to build.

Time complexity would be as much as we can generate the n! permutations which
is O(n! * n^2).

---

Java:

```java

class Solution46 {

    List<List<Integer>> result;
    int[] nums;

    public List<List<Integer>> permutations(int[] nums)
    {
        this.nums = nums;
        this.result = new ArrayList<>();
        helper(0);

        return this.result;
    }

    private void helper(int start)
    {
        if (start == this.nums.length) {
            List<Integer> path = new ArrayList<>();
            for (int num : this.nums)
                path.add(num);
            this.result.add(path);
        } else {
            for (int i = start; i < this.nums.length; i++)
            {
                swap(i, start);
                helper(start + 1);
                swap(i, start);
            }
        }
    }

    private void swap(int i, int j)
    {
        int temp = this.nums[i];
        this.nums[i] = this.nums[j];
        this.nums[j] = temp;
    }
}

```
