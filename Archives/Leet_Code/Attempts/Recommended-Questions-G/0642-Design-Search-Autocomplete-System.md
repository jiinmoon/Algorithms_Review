# 642. Design Search Autocomplete System

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

For each of the characters typed, we need to update the list of matching
sentences. Thus, we need a queue to store the previous characters that user has
typed so far as well as a queue of matching sentences.

When new character is typed, we can go through the history of the sentences and
build the matching sentences list. We sort the list so that we have it sorted
by its count. For subsequent characters, we can simply iterate and update the
matching sentences so long as the new char is at the correct index of the
sentences. When terminated by "#", we discard the reset the matching sentences
list and add our current built user search word to our history record count.

---

Python:

```python

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.d = collections.defaultdict(int)
        for s, t in zip(sentences, times):
            self.d[s] = t
        self.userInput = list()
        self.matching = list()

    def input(self, char):
        if char == "#":
            self.d["".join(self.userInput)] += 1
            self.userInput = list()
            self.matching = list()
            return
        if not self.userInput:
            self.matching = [(-c, s) for s, c in self.d.items() if s[0] == char]
            self.matching.sort()
            self.matching = [s for _, s in self.matching]
        else:
            i = len(self.userInput)
            self.matching = [s for s in self.matching if len(s) > i and s[i] == char]
        self.userInput
        return self.matching[:3]
```

