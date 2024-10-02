class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        dd = defaultdict(deque)
        for i, c in enumerate(word1):
            dd[c].append(i)
        d = deepcopy(dd)

        # Can Create
        w2_idx, w1_idx = -1, -1
        ans, life = [], True
        for i, c in enumerate(word2):
            while len(d[c]) and d[c][0] <= w1_idx:
                d[c].popleft()
            if len(d[c]) == 0:
                if not life or w1_idx == len(word1)-1:
                    break
                life = False
                d[c].append(w1_idx + 1)

            ans.append(d[c].popleft())
            w2_idx, w1_idx = i, ans[-1]

        if len(ans) == len(word2):
            if life:
                for i in range(len(word2)):
                    if ans[i] != i:
                        ans[i] = i
                        break

        d = defaultdict(deque)
        word1 = list(word1)
        # Use the life on the first char
        word1[0] = word2[0]
        word1 = ''.join(word1)

        for i, c in enumerate(word1):
            d[c].append(i)

        ans2 = []
        w1_idx = -1
        for i, c in enumerate(word2):
            while len(d[c]) and d[c][0] <= w1_idx:
                d[c].popleft()
            if len(d[c]) == 0:
                break
            ans2.append(d[c].popleft())
            w1_idx = ans2[-1]

        if len(ans2) == len(word2):
            ans = min(ans, ans2)

        return ans if len(ans) == len(word2) else []
