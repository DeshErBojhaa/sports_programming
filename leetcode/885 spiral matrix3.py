def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def in_range(i, j):
            return i >= 0 and i < R and j >= 0 and j < C
        
        horizontal, vertical = 1, 1
        cnt, mv_no = 1, 1
        ans = [[r0,c0]]
        while cnt < R*C:
            # print(r0, c0)
            if mv_no == 1:
                horizontal += 1
                for i in range(c0+1, c0+horizontal):
                    if in_range(r0, i):
                        cnt += 1
                        ans.append([r0, i])
                c0 += horizontal - 1
            if mv_no == 4:
                vertical += 1
                for i in range(r0-1, r0-vertical, -1):
                    if in_range(i, c0):
                        cnt += 1
                        ans.append([i, c0])
                r0 -= (vertical - 1)
            if mv_no == 3:
                horizontal += 1
                for i in range(c0-1, c0-horizontal, -1):
                    if in_range(r0, i):
                        cnt += 1
                        ans.append([r0, i])
                c0 -= (horizontal - 1)
            if mv_no == 2:
                vertical += 1
                for i in range(r0+1, r0+vertical):
                    if in_range(i, c0):
                        cnt += 1
                        ans.append([i, c0])
                r0 += (vertical - 1)
            mv_no = (mv_no + 1)%5
        return ans
