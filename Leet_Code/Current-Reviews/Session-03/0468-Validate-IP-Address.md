468 Validate IP Address
=======================

Given a string `IP`, return `IPv4` if IP is a valid IPv4, return `IPv6` if IP
is a valid IPv6. Else, return `neither`.

---

First we check for whether the string is a valid IPv4 by spliting on periods
and check whether each segment is within the range of 0 ~ 255.

Next, check for valid IPv6 by spliting on colon. Then, check each segment for
whether they fall within the valid range 0 ~ FFFF.

Else, we return "neither".

---

Python:

```python

class Solution:
    def validIPAddress(self, IP):
        # check IPv4
        ipv4 = IP.split(".")
        if len(ipv4) == 4:
            for seg in ipv4:
                # try decimal conversion; if fails, it is not valid
                try:
                    intSeg = int(seg)
                except ValueError:
                    return "Neither"
                # segment in range 0 ~ 255 and does not have leading zeros
                if intSeg < 0 or intSeg > 255 or len(str(intSeg)) != len(seg):
                    return "Neither"
            return "IPv4"

        # check IPv6
        ipv6 = IP.split(":")
        if len(ipv6) == 8:
            for seg in ipv6:
                # try hex conversionl if it fails, it is not valid
                try:
                    hexSeg = int(seg, 16)
                except ValueError:
                    return "Neither"
                # segment in range 0 ~ FFFF and does not have leading zeros
                if hexSeg < 0 or hexSeg > int("FFFF", 16) or len(seg) > 4:
                    return "Neither"
            return "IPv6"

        return "Neither"
```
