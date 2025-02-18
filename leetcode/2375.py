class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = [9] * (n + 1)

        def rec(arr, mask):
            nonlocal ans
            if arr > ans:
                return
            if mask == 1:
                ans = arr[:]
                return
            patt_idx = len(arr)
            inc = patt_idx and pattern[patt_idx - 1] == 'I'
            for i in range(1, 10):
                if mask & (1<<i) == 0:
                    continue
                if patt_idx == 0:
                    arr.append(i)
                    rec(arr, mask ^ (1<<i))
                    arr.pop()
                    continue
                
                last = arr[-1]
                if inc and last < i:
                    arr.append(i)
                    rec(arr, mask ^ (1<<i))
                    arr.pop()
                if not inc and last > i:
                    arr.append(i)
                    rec(arr, mask ^ (1<<i))
                    arr.pop()
        
        mask = (1 << (n + 2)) - 1
        rec([], mask)

        return ''.join(map(str, ans))




