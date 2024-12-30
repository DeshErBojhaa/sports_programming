class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        ans = 1
        MOD = 10**9 + 7
        cnt_arr = []
        for i, ch in enumerate(words[0]):
            cnt = Counter()
            for w in words:
                cnt[w[i]] += 1
            cnt_arr.append(cnt)
            
        N, M = len(words[0]), len(target)
        
        @lru_cache(None)
        def rec(a, b):
            if b == M:
                return 1
            if a == N:
                return 0
            
            ans = 0
            now_ch = target[b]
            cc = cnt_arr[a][now_ch]
            ans = rec(a+1, b+1) * cc
            ans += rec(a+1, b)
            
            return ans % MOD
        
        return rec(0, 0)
            
