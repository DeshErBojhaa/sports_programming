# 1255. Maximum Score Words Formed by Letters
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        w_scores = [sum(map(lambda x: score[ord(x) - ord('a')], w)) for w in words]
        letter_count = Counter(letters)
        w_counter = [Counter(w) for w in words]

        N, ans = len(words), 0

        for mask in range(2**N):
            tmp_ans, cur_letter_count = 0, Counter()
            for i in range(N):
                if mask & (1<<i) == 0:
                    continue
                tmp_ans += w_scores[i]
                cur_letter_count += w_counter[i]

                for ch, cnt in cur_letter_count.items():
                    if cnt > letter_count[ch]:
                        break
                else:
                    continue
                break
            else:
                ans = max(ans, tmp_ans)

        return ans
