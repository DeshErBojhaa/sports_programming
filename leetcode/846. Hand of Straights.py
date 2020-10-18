# 846. Hand of Straights
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        nums, k = hand, W
        c = Counter(nums)
        startnums = [x for x in c if not c[x-1]]
        
        while startnums:
            start = startnums.pop()
            for v in reversed(range(start, start + k)):
                c[v] -= c[start]
                if c[v] < 0:
                    return False
                if not c[v] and c[v+1]:
                    startnums.append(v+1)
        
        return True
