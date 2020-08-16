# 1551. Minimum Operations to Make Array Equal
class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2*i)+1 for i in range(n)]
        mid = n // 2
        
        l = sum(arr[:mid])
        r = sum(arr[mid+(n&1):])
        # print(arr, l, r)
        return (r-l)//2
