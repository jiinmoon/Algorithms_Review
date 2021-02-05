# 854. K-Similar Strings

Strings A and B are K-similar (for some non-negative integer K) if we can swap
the positions of two letters in A exactly K times so that the resulting string
equals B.

Given two anagrams A and B, return the smallest K for which A and B are
K-similar.

---

Let's think of this problem as a graph problem where we are trying to find the
shortest path from A to B where each node is words where two letters are
swapped. Then, we can use BFS algorithm where we make swaps at each depth to
check for whether we have successfully swapped letters in A to form B in minmal
number of steps.

Then, at each step, we examine the current nodes in our queue.

Current word can be transformed to by swapping two letters; the index where
swap should occur must be starting from the first index where the characters do
not agree with each other (current node and the goal node). Once the first
index where the characters do not agree has been found, we have to try all
possible swaps starting from that position so long as they do not agree with
each other.

Time complexity would be O(n! * n) since we have to examine all possible swaps
in worst case at each depth.

---

Java:

```java

class Solution854 {

    public int kSimilarity(String A, String B)
    {
        // invalid cases
        if (A == null || B == null || A.equals(B) || A.length() != B.length())
            return 0;
        
        List<String> queue = new ArrayList<>(List.of(A));
        Set<String> visited = new HashSet<>(); 
        int k = 1;

        while (!queue.isEmpty())
        {
            List<String> temp = new ArrayList<>();

            for (String word : queue)
            {
                // find start index where two words to not agree
                int i = 0;
                while (i < word.length() && word.charAt(i) == B.charAt(i))
                    i++;

                // starting from this position, swap every possible position
                for (int j = i + 1; j < word.length(); j++)
                {
                    // invalid cases
                    if (word.charAt(j) != B.charAt(i) || word.charAt(j) == word.charAt(j))
                        continue;

                    // swap
                    char[] charsWord = word.toCharArray();
                    char temp = charsWord[i];
                    charsWord[i] = charsWord[j];
                    charsWord[j] = temp;
                    String swappedWord = String.valueOf(charsWord);

                    // goal
                    if (B.equals(swappedWord))
                        return k;

                    if (visited.contains(swappedWord))
                        continue;

                    temp.add(swappedWord);
                    visited.add(swappedWord);
                }
            }

            queue = temp;
            k++;
        }

        return -1;      // error reaching here;
    }
}

```
