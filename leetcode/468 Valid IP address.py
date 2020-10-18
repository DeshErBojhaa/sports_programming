# 468 Valid IP address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def v4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for p in parts:
                if not p:
                    return False
                if p[0] == '0' and p[-1] != '0':
                    return False
                if len(p) > 1 and p[0] == '0' or p[0] == '-':
                    return False
                val = None
                try:
                    val = int(p)
                except Exception as e:
                    return False
                if val is None or val < 0 or val > 255:
                    return False
            return True
        
        def v6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            for p in parts:
                print(p)
                if not p:
                    return False
                if len(p) > 4 or p[0] == '-':
                    return False
                val = None
                try:
                    val = int(p, 16)
                except Exception as e:
                    return False
                if val is None or val < 0 or val > 65535:
                    return False
            return True
        
        if v4(IP):
            return "IPv4"
        if v6(IP):
            return "IPv6"
        return "Neither"
