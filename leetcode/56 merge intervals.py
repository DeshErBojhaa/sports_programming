class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        i = sorted(intervals)
        st, en = i[0][0], i[0][1]
        ans = []
        for s, e in i:
            if s <= en:
                en = max(e, en)
            else:
                ans.append([st, en])
                st = s
                en = e
        ans.append([st,en])
        
        return ans
