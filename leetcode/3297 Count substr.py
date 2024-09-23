class Solution:
    def validSubstringCount(self, w: str, ww: str) -> int:
        covered, c = False, Counter(ww)
        ans = 0
        heap, cc, heap_cc = [], Counter(), Counter()

        def ok():
            for ch_, v in c.items():
                if cc[ch_] < v:
                    return False
            return True

        for i, ch in enumerate(w):
            cc[ch] += 1
            if ch in c:
                heappush(heap, [i, ch])
                heap_cc[ch] += 1

            while heap and heap_cc[heap[0][1]] > c[heap[0][1]]:
                    _, x = heappop(heap)
                    heap_cc[x] -= 1

            if not covered:
                covered = ok()
            if covered:
                right = heap[0][0]
                ans += right
                ans += 1

        return ans
