class Solution:
    def getSkyline(self, b: List[List[int]]) -> List[List[int]]:
        arr = []
        for i, (l, r, h) in enumerate(b):
            arr.append((l, 'l', -h, i))
            arr.append((r, 'r', -h, i))
        arr.sort()

        heap = []
        obsolete, point, ans = set(), (0, 0), []
        for line, sign, h, idx in arr:
            if sign == 'l':
                heappush(heap, (h, idx))
                new_point = [line, -heap[0][0]]
                if point[1] < new_point[1]:
                    point = new_point
                    ans.append(point)
                continue

            obsolete.add(idx)
            while heap and heap[0][1] in obsolete:
                heappop(heap)

            new_point = [line, -heap[0][0] if heap else 0]
            if point[1] > new_point[1]:
                if point[0] == new_point[0]:
                    ans[len(ans)-1][1] = new_point[1]
                else:
                    ans.append(new_point)
                point = new_point

        return ans
