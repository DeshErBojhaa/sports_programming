# 1153. String Transforms Into Another String
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        d = {}
        
        for a, b in zip(str1, str2):
            if a not in d:
                d[a] = b
            if d[a] != b:
                return False
        
        return len(set(str2)) < 26
