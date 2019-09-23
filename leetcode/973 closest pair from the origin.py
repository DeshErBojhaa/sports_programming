def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l = sorted(points, key=lambda p: p[0]**2 + p[1]**2)
        return l[:K]
