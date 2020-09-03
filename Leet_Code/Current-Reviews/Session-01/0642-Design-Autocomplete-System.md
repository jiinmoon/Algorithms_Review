642 Design Autocomplete System
==============================

Design a search autocomplete system for a search engine. Users may input
a sentence (at least one word and end with a special character '#'). For each
character they type except '#', you need to return the top 3 historical hot
sentences that have prefix the same as the part of sentence already typed. Here
are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed
the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is
the hottest one). If several sentences have the same degree of hot, you need to
use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this
case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor.
The input is historical data. Sentences is a string array consists of
previously typed sentences. Times is the corresponding times a sentence has
been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will
provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the
user. The character will only be lower-case letters ('a' to 'z'), blank space
(' ') or a special character ('#'). Also, the previously typed sentence should
be recorded in your system. The output will be the top 3 historical hot
sentences that have prefix the same as the part of sentence already typed.

---

We will maintain the user input as well as the sentences that which matches
with the user input so far.

---

Python:

```python
from collections import defaultdict

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.userInput = list()
        self.matchingStr = list()
        self.counter = defaultdict(int)
        for s, t in zip(sentences, times):
            self.counter[s] = t

    def input(self, c):
        # case:1 end of user input
        # save the current user input back to the counter
        if c == '#':
            curr = "".join(self.userInput)
            self.counter[curr] += 1
            self.userInput = list()
            self.matchingStr = list()
            return
        # case:2 start of new user input
        # initialize the matchingStr from counter that matches first char
        if not self.userInput:
            # negative times for max->min ordering
            self.matchingStr = [ (-t, s) for s, t 
                                    in self.counter.items() if
                                    s[0] == c
            ]
            self.matchingStr.sort()
            self.matchingStr = [ x[1] for x in self.matchingStr ]
        
        # case:3 update the machingStr based on additional char
        else:
            i = len(self.userInput)
            self.machingStr = [ s for s in self.matchingStr 
                                if len(s) > i and s[i] == c 
            ]

        self.userInput.append(c)
        return self.matchingStr[:3]
```
