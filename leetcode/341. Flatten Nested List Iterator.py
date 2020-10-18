# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
# 341. Flatten Nested List Iterator
from collections import deque
class NestedIterator:
    def flat(self, l):
        ans = []
        for x in l:
            if x.isInteger():
                ans.append(x.getInteger())
            else:
                ans.extend(self.flat(x.getList()))
                
        return ans
    
    def __init__(self, nestedList: [NestedInteger]):
        self.dq = deque()
        for nl in nestedList:
            if nl.isInteger():
                self.dq.append(nl.getInteger())
            else:
                self.dq.extend(self.flat(nl.getList()))
            
    def next(self) -> int:
        return self.dq.popleft()
    
    def hasNext(self) -> bool:
         return len(self.dq) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
