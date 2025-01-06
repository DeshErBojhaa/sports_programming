class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        ans = [0] * (N + 1)
        ans2 = [0] * (N + 1)
        balls = 0
        for i in range(N-1, -1, -1):
            ans[i] = ans[i+1] + balls
            balls += int(boxes[i] == '1')
        
        balls = 0
        for i in range(N):
            ans2[i] += ans2[i-1] + balls
            balls += int(boxes[i] == '1')
        
        return [a+b for a, b in zip(ans[:-1], ans2[:-1])]
