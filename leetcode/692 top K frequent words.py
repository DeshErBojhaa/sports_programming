from collections import Counter
class Solution:
    def topKFrequent(self, w: List[str], k: int) -> List[str]:
        c = Counter(w)
        _stack = []

        for a,b in c.items():
            tmp_stack = [] # (str, cnt)
            while _stack and _stack[-1][1] < b:
                tmp_stack.append(_stack.pop())
            while _stack and _stack[-1][1] == b and _stack[-1][0] > a:
                tmp_stack.append(_stack.pop())
            _stack.append((a, b))
            while tmp_stack:
                _stack.append(tmp_stack.pop())
        return [m[0] for m in _stack[:k]]
