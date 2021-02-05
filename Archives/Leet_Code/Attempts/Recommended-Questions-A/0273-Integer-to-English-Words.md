# 273. Integer to English Words

Convert a non-negative integer num to its English words representation.

---

To convert the given integer into English words, we first create a mapping
between each integer (0-20, 30, 40, 50, 60, 70, 80, 90) as well as the digits
(Thousand, Million, Billion, ...). Then, we use modulo operation to iterate on
the given num at every thousand digit (3 digits) to build on the English word
with mapping created.

---

Java:

```java

class Solution {
    Map<Integer, String> intMap;
    Map<Integer, String> digitMap;

    public Solution() {
        this.intMap = new HashMap<>();
        intMap.put(1, "One");       intMap.put(2, "Two");
        intMap.put(3, "Three");     intMap.put(4, "Four");
        intMap.put(5, "Five");      intMap.put(6, "Six");
        intMap.put(7, "Seven");     intMap.put(8, "Eight");
        intMap.put(9, "Nine");      intMap.put(10, "Ten");
        intMap.put(11, "Eleven");   intMap.put(12, "Twelve");
        intMap.put(13, "Thirteen"); intMap.put(14, "Fourteen");
        intMap.put(15, "Fifteen");  intMap.put(16, "Sixteen");
        intMap.put(17, "Seventeen");intMap.put(18, "Eighteen");
        intMap.put(19, "Nineteen"); intMap.put(20, "Twenty");
        intMap.put(30, "Thirty");   intMap.put(40, "Forty");
        intMap.put(50, "Fifty");    intMap.put(60, "Sixty");
        intMap.put(70, "Seventy");  intMap.put(80, "Eighty");
        intMap.put(90, "Ninety");

        this.digitMap = new HashMap<>();
        digitMap.put(3, "Thousand");
        digitMap.put(6, "Million");
        digitMap.put(9, "Billion");
    }
    
    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        
        List<String> result = new ArrayList<>();
        int digit, thousand, hundred, ten;
        digit = 0;

        while (num != 0) {
            thousand = num % 1000;
            ten = thousand % 100;
            num /= 1000;
            hundred = thousand / 100;

            if (digit > 0 && thousand > 0) result.add(this.digitMap.get(digit));
            digit += 3;
            
            if (ten != 0) {
                if (ten <= 20) {
                    result.add(intMap.get(ten));
                } else {
                    if (ten % 10 != 0) result.add(intMap.get(ten % 10));
                    result.add(intMap.get(10 * (ten / 10)));
                }
            }
            
            if (hundred > 0) result.add(intMap.get(hundred) + " Hundred");
        }
        Collections.reverse(result);
        return String.join(" ", result);
    }
}

```

Python:

```python

class Solution:
    def numberToWords(self, num):
        intMap = {
            1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
            6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
            11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
            15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
            19 : 'Nineteen', 20 : 'Twenty', 30 : 'Thirty', 40 : 'Forty',
            50 : 'Fifty', 60 : 'Sixty', 70 : 'Seventy', 80 : 'Eighty',
            90 : 'Ninety'
        }
        digitMap = {
            3 : 'Thousand', 6  : 'Million', 9 : 'Billion', 12 : 'Trillion',
            15 : 'Quadrillion', 18 : 'Quintillion', 21 : 'Sextillion',
            '24' : 'Septillion', 27 : 'Octillion', 30 : 'Nonillion'
        }
        
        result = collections.deque()
        digit = 0
        while num:
            num, thousand = divmod(num, 1000)
            hundred, ten = divmod(thousand, 100)

            if not digit or thousand:
                result.appendleft(digitMap[digit])
            digit += 3
            
            if ten <= 20:
                result.appendleft(intMap[ten])
            else:
                if ten % 10:
                    result.appendleft(intMap[ten % 10])
                result.appendleft(intMap[10 * (ten // 10)])

            if hundred:
                result.appendleft("Hundred " + intMap[hundred])

        return " ".join(result)
```
