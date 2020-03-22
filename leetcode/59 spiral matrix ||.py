class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        ans = [[-1]*n for _ in range(n)]
        turn, num = 0, 1
        
        while num <= n*n:
            
            active_row = (turn//4)
            for i in range(n):
                if ans[active_row][i] == -1:
                    ans[active_row][i] = num
                    num += 1
                if num > n*n:
                    break
            turn+= 1
            
            # Rotate anti clockwise
            ans = list(list(xx) for xx in zip(*ans))[::-1]
        
        while ans[0][0] != 1:
            ans = list(list(xx) for xx in zip(*ans))[::-1]

        return ans
        
