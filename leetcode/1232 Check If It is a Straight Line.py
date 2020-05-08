class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(set(x[0] for x in coordinates)) == 1 or len(set(x[1] for x in coordinates)) == 1:
            return True
        if len(coordinates) < 3:
            return True
        
        dely = abs(coordinates[0][1] - coordinates[1][1])
        delx = abs(coordinates[0][0] - coordinates[1][0])
        
        for a, b in zip(coordinates[1:], coordinates[2:]):
            dy = abs(a[1] - b[1])
            dx = abs(a[0] - b[0])
            
            if dely * dx != delx * dy:
                return False
        
        return True
