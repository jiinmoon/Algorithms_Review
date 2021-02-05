# 468 Validate IP Address

class Solution:
    def validateIP(self, IP):
        ipv4 = IP.split(".")
        if len(ipv4) == 4:
            for seg in ipv4:
                try:
                    iseg = int(iseg)
                except ValueError:
                    return "Neither"
                if not (0 <= iseg <= 255) and not len(str(iseg)) == len(seg):
                    return "Neither"
            return "IPv4"
        
        ipv6 = IP.split(":")
        if len(ipv6) == 8:
            for seg in ipv6:
                try:
                    hseg = int(seg, 16)
                except ValueError:
                    return "Neither"
                if not (0 <= hseg <= int("FFFF", 16)) and not len(seg) == 4:
                    return "Neither"
            return "IPv6"

        return "Neither"
