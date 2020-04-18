class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        
        while len(v1) < len(v2):
            v1.append(0)
        while len(v2) < len(v1):
            v2.append(0)
        
        for a, b in zip(v1, v2):
            if a > b:
                return 1
            if b > a:
                return -1
        return 0
