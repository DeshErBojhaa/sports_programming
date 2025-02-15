class Solution:
    def punishmentNumber(self, n: int) -> int:
        @cache
        def rec(num, target):
            if num == target:
                return True
            if num < target:
                return False
            if num == 0 and target == 0:
                return True
            if num <= 0 or target <= 0:
                return False
            
            cum, pw = 0, 0

            while num:
                mlt = 10 ** pw
                cum += mlt * (num % 10)
                num //= 10
                pw += 1
                if rec(num, target - cum):
                    return True
            return False
        
        # rec(36 * 36, 36)
        ans = 0
        for i in range(1, n+1):
            if rec(i * i, i):
                ans += i * i
        return ans


