from collections import Counter
from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = heapq.nlargest(k, c.items(), key=itemgetter(1))
        return [x[0] for x in ans]
