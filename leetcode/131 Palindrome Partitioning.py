# 131. Palindrome Partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def rec(ss, partitions):
            if not ss:
                ans.append(partitions[::1])
                return
            
            for i in range(len(ss)):
                if ss[:i+1] == ss[:i+1][::-1]:
                    partitions.append(ss[:i+1])
                    rec(ss[i+1:], partitions)
                    partitions.pop()

        rec(s, [])
        return ans
