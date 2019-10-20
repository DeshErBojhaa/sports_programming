def checkStraightLine(self, c: List[List[int]]) -> bool: # x,y
        if c[0][0] - c[1][0] == 0: # delta X 0 Y must be on same line
            return all(y1[1] == y2[1] for y1, y2 in zip(c, c[1:]))
        if all(y1[1] == y2[1] for y1, y2 in zip(c, c[1:])):
            return True
        
        x1 = c[1][0] - c[0][0]
        y1 = c[1][1] - c[0][1]
        
        for i in range(2, len(c)):
            dx = c[i][0] - c[i-1][0]
            dy = c[i][1] - c[i-1][1]
            
            if dx * y1 != x1 * dy:
                return False
        
        return True
