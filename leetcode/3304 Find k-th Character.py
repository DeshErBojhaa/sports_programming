class Solution:
    def kthCharacter(self, k: int) -> str:
        l = ['a']
        while len(l) < k:
            n = l[::]
            for i in range(len(n)):
                n[i] = chr((ord(n[i]) + 1) % ord('z'))
            l += n
        
        return l[k-1]
