# 365. Water and Jug Problem
from queue import SimpleQueue
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x+y:
            return False
        
        q = SimpleQueue()
        q.put((0,0))
        seen = set((0,0))
        
        while q.qsize():
            a, b = q.get()
            if a == z or b == z or a + b == z:
                return True
            
            # Fill a
            state = (x, b)
            if state not in seen:
                seen.add(state)
                q.put(state)
            
            # Fill b
            state = (a, y)
            if state not in seen:
                seen.add(state)
                q.put(state)
            
            # Pour a -> b
            rem_y = y - b
            poure_amount = min(rem_y, a)
            state = (a-poure_amount, b + poure_amount)
            if state not in seen:
                seen.add(state)
                q.put(state)
            
            
            # Pour a <- b
            rem_x = x - a
            poure_amount = min(rem_x, b)
            state = (a + poure_amount, b - poure_amount)
            if state not in seen:
                seen.add(state)
                q.put(state)
            
            # Empty a
            state = (0, b)
            if state not in seen:
                seen.add(state)
                q.put(state)
            
            # Empty b
            state = (a, 0)
            if state not in seen:
                seen.add(state)
                q.put(state)
        
        return False
            
        
