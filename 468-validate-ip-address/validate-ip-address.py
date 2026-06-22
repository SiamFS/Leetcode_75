class Solution(object):
    def validIPAddress(self, queryIP):
        if '.' in queryIP:
            return "IPv4" if self.isIPv4(queryIP) else "Neither"
        else:
            return "IPv6" if self.isIPv6(queryIP) else "Neither"

    def isIPv4(self, ip):
        parts = ip.split(".")

        if len(parts) != 4:
            return False

        for part in parts:
            if not part:
                return False
            if not part.isdigit():
                return False
            if len(part) > 1 and part[0] == "0":
                return False
            if not (0 <= int(part) <= 255):
                return False

        return True

    def isIPv6(self, ip):
        parts = ip.split(":")

        if len(parts) != 8:
            return False

        for part in parts:
            if not (1 <= len(part) <= 4):
                return False

            for ch in part:
                if ch not in "0123456789abcdefABCDEF":
                    return False

        return True