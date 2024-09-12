class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        arr = [(d, h) for d, h in zip(damage, health)]

        def cmp(a, b):
            da, ha = a
            db, hb = b
            ta = ceil(ha/power)  # Turn to kill a
            tb = ceil(hb/power)  # Turn to kill b

            # Kill a first              >   Kill b first
            if da * ta + db * ta + db * tb >= da * ta + da * tb + db * tb:
                return 1
            return -1
        
        arr.sort(key=cmp_to_key(cmp))

        ans, cum = 0, 0
        for d, h in arr:
            cum += ceil(h/power)
            ans += cum * d
        
        return ans
