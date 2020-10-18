# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y
# 1274. Number of Ships in a Rectangle
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def calc(x, X, y, Y):
            if x > X or y > Y or not sea.hasShips(Point(X,Y), Point(x,y)):
                return 0
            if (x,y) == (X, Y):
                return 1
            
            mr, mc = (x + X)//2, (y+Y)//2
            
            xRange = (x, mr), (mr+1, X)
            yRange = (y, mc), (mc+1, Y)
            
            return sum(calc(*nx, *ny) for nx in xRange for ny in yRange)
            
        return calc(bottomLeft.x, topRight.x, bottomLeft.y, topRight.y)
