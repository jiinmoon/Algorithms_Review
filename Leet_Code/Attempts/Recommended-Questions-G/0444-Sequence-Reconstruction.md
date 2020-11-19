# 444. Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the
sequences in seqs. The org sequence is a permutation of the integers from 1 to
n, with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common
supersequence of the sequences in seqs (i.e., a shortest sequence so that all
sequences in seqs are subsequences of it). Determine whether there is only one
sequence that can be reconstructed from seqs and it is the org sequence.

---

Let's consider few examples to help our understanding.

org = [1,2,3]
seq = [[1,2],[1,3],[2,3]]

Try to build according to the reconstruction rule, we see that 1 has to come
before 2 and 3 hence it is our first value. Then, we also discover that 2 comes
after 2 and before 3. Lastly, 3.

Suppose seq like [[1,2], [1,3]]. In this case, order of 2 and 3 is unclear.
Hence, it creates further non-unique permutations such as [1,2,3] as well as
[1,3,2].

So, we need to check for individual values present, "but" also their relative
positions on the org.

To do so, let's create a index map where it tells where the values appear for
each of the numbers. But since we need to determine the order, we collect the
numbers in pairs: i.e. given [1,2,3], the collected pairs should be [1,2],
[2,3]. However, there may be an edge case where given original string length is
only 1 - in which case cannot form pairs. For this case, we also add additional
marker to denote the beginning pair to tell the order.

Then, we go through each of the sequences. For each given sequence, we examine
the pairs to find the orders of the characters present within the orders. If
the values are not found or we find their order relative to our original string
is wrong (second char in seq appears before first char in seq compared to
original) we can determine that ordering is wrong and cannot reconstruct.
Otherwise, we can delete our current pairs as they are used to form.

In the end, there should not be any pairs leftover to form.

In terms of time complexity, we first need to iterate on original string to
construct our index map in hashmap; also, we have to go through each sequence.
Hence, time complexity should be O(m + k) where m is length of original and
k is sum of all sequences length.

---

Python:

```python

class Solution:
    def sequenceReconstruction(self, org, seqs):
        # all the pairs in order must be covered
        pairsToForm = {(c1, c2) for zip([None] + org, org)}
        order = {c:i for i, c in enumerate([None] + org)}

        for seq in seqs:
            for c1, c2 in zip([None] + seq, seq):
                # fails when values are not present or
                # order of characters in pairs is wrong
                if c1 not in order or c2 not in order or order[c1] >= order[c2]:
                    return False
                # current sequence pair is valid;
                # use to build our segment
                pairsToForm.discard((c1, c2))

        return not pairsToForm
```

