class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_count = Counter(words)
        word_len = len(words[0])
        total_len = word_len * len(words)
        N, WN = len(s), len(words)

        invalid = set()

        def ok(idx):
            if idx + total_len > N:
                return False
            substr = s[idx: idx+total_len]
            if substr in invalid:
                return False
            c = Counter()
            for i in range(idx, idx+total_len, word_len):
                ss = s[i: i+word_len]
                if ss not in word_count:
                    return False
                c[ss] += 1

            if c != word_count:
                invalid.add(substr)
            return c == word_count

        ans, i = [], 0
        while i < N:
            if ok(i):
                ans.append(i)
            i += 1

        return ans
