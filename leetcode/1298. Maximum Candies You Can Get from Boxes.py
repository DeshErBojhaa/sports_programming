# 1298. Maximum Candies You Can Get from Boxes
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        ans = 0
        seen = set()
        av_keys = set()
        
        q = deque(initialBoxes)
        for x in initialBoxes:
            av_keys |= set(keys[x])
        
        while q:
            now = q.popleft()
            seen.add(now)
            if not status[now] and now not in av_keys:
                continue

            av_keys |= set(keys[now])
            ans += candies[now]
            
            for nxt in containedBoxes[now]:
                if nxt in seen:
                    continue
                if status[nxt] or nxt in av_keys:
                    q.appendleft(nxt)
                else:
                    q.append(nxt)
        
        return ans
