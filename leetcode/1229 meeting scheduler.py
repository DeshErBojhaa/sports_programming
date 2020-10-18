def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1)
        slots2 = sorted(slots2)
        a, b, l1, l2 = 0, 0, len(slots1), len(slots2)
        ans = []
        while a < l1 and b < l2:
            st = max(slots1[a][0], slots2[b][0])
            ed = min(slots1[a][1], slots2[b][1])
            
            if ed - st >= duration:
                return [st, st+duration]
            
            if slots1[a][1] > slots2[b][1]:
                b += 1
            else:
                a += 1
        return []
