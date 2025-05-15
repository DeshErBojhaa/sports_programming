class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        cur = groups[0]
        for i, g in enumerate(groups):
            if g != cur:
                continue
            ans.append(words[i])
            cur = 1 - cur
        return ans
