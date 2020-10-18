# 1349. Maximum Students Taking Exam
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        N, M = len(seats), len(seats[0])
            
        def invalid(r, c, cur, prev):
            if c and (cur & (1<<(c-1)) or prev & (1<< (c-1))):
                # print(r,c, bin(cur), bin(prev), 'Right Buddy')
                return True
            if c + 1 < M and (cur & (1<<(c+1)) or prev & (1<<(c+1))):
                # print(r,c, bin(cur), bin(prev), 'Left Buddy', cur & (1<<(c+1)))
                return True
            
            return False
        
        @lru_cache(None)
        def rec(cur, prev_mask):
            if cur == N:
                return 0
            # print(cur, bin(prev_mask))
            ans = 0
            for cur_mask in range((1<<M)):
                for i in range(M):
                    if cur_mask & (1<<i) == 0:
                        continue
                    if (cur_mask & (1<<i)) and seats[cur][M-i-1] == '#':
                        break
                    if invalid(cur, i, cur_mask, prev_mask):
                        break
                else:
                    ans = max(ans, rec(cur+1, cur_mask) + bin(cur_mask).count('1'))
                    
            return ans
        
        return rec(0, 0)
