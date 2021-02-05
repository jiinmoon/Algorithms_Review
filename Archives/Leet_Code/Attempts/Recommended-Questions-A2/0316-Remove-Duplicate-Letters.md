# 316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once
and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

---

We use a stack to build our result. As we iterate on the given string, we check
for following conditions:

(1) char is already in stack; this indicates a duplicate so we ignore.

(2) top of our stack is lexicographically greater than current character *AND*
it appears later in the string than our current character; we can form
a lexicographically smaller string by removing the top of stack.

(3) otherwise, new character is added to our result.

Time and space complexity would be O(n); it may appear to be O(n^2) due to the
fact that we have to check whether character is in the stack, but we are only
maintaining *UNIQUE* characters - thus size is limited to O(26).

---

Java:

```java

class Solution316 {

    public String removeDuplicate(String s)
    {
        int[] lastIndex = new int[26];
        for (int i = 0; i < s.length(); i++)
            lastIndex[s.charAt(i) - 'a'] = i;

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++)
        {
            char curr = s.charAt(i);
            if (result.lastIndexOf(Character.toString(curr)) != -1)
                continue;
            while (result.length() > 0 && 
                    result.charAt(result.length() - 1) > curr && 
                    lastIndex[result.charAt(result.length() - 1) - 'a'] > i)
                result.deleteCharAt(result.length() - 1);
            result.append(curr);
        }

        return result.toString();
    }
}

```
