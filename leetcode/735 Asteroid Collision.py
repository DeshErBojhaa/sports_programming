# 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if a >= 0:
                stack.append(a)
                continue
            
            do_append = True
            while stack and stack[-1] >= 0:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    stack.pop()
                    do_append = False
                    break
                else:
                    do_append = False
                    break
            
            if do_append:        
                stack.append(a)
        
        return stack
