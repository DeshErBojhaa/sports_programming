class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        for ch in s:
            if ch == ']':
                if left == 0:
                    left += 1
                    continue
                left -= 1
            else:
                left += 1
        return left // 2
