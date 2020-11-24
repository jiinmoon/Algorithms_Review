# Unique Device Names

You are working on the Amazon Devices team and need to create unique device
names to be used in a residential loT (Internet of Things) system. If a device
name already exists in the system, an integer number is added at the end of the
name to make it unique. The integer added starts with land is incremented by
1 for each new request of an existing device name.
Given a list of device name requests, write an algorithm to process all the
requests and output a list of the corresponding unique device names.

Input
The input to the function/method consists of two arguments:
num, an integer representing the number of device names;
devicenames, a list of strings representing the device names;

Output
Return a list of strings representing the usernames in the order assigned

Constraints
1 <= num <= 10^5
1 <= length of devicenames[i] >= 20
0 <= i < num

Note
devicenames contains only lowercase English letters in the range ASCII[a-z].

---

Use a hashmap to store (item, itemNum). As we exaimne each item, we check
against our hashmap to see its current itemNum and add to result.

Time and space complexity are O(n).

---

Python:

```python

class Solution:
    
    def uniqueDeviceNames(items, n):
        if (n <= 1):
            return items

        m = collections.defaultdict(int)
        result = list()

        for item in items:
            itemNum = m[item]
            currItem = item if not itemNum else item + str(itemNum)
            result.append(currItem)
            m[item] += 1;

        return result
```

Java:

```java

class Solution {

    public String[] uniqueDeviceNames(String[] items, int n) {
        if (n <= 1) 
            return items;

        HashMap<String, Integer> map = new HashMap<>();
        String[] result = new String[n];
        int i = 0;

        for (String item : items) {
            int itemNum = map.getOrDefault(item, 0);
            result[i++] = (itemNum == 0) ? item : item + itemNum;
            map.put(item, ++itemNum);
        }
        
        return result;
    }
}
