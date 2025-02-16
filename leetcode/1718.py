class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        nn = (n * 2) - 1
        ans = []

        def rec(arr, mask):
            nonlocal ans
            if ans > arr:
                return
            if mask == 1:
                
                if arr > ans:
                    ans = arr[:]
                return

            cur_idx = arr.index(-1)
            for i in range(n, 0, -1):
                if mask & (1 << i) == 0:
                    continue
                if i!= 1 and (cur_idx + i >= len(arr) or arr[cur_idx + i] != -1):
                    continue
                arr[cur_idx] = i
                if i != 1:
                    arr[cur_idx + i] = i
                rec(arr, mask ^ (1<<i))
                arr[cur_idx] = -1
                if i != 1:
                    arr[cur_idx + i] = -1
        
        rec([-1] * nn, (2 ** (n+1) - 1))
        return ans

