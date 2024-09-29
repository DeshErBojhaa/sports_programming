class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        w = [None] * len(word)
        vowels = set('aeiou')
        for i, ch in enumerate(word):
            if ch in vowels:
                w[i] = ch
                continue
            w[i] = '#'
        word = ''.join(w)

        pos, l = defaultdict(deque), 0
        ans = 0

        for i, ch in enumerate(word):
            pos[ch].append(i)

            while len(pos['#']) > k:
                c = word[l]
                if len(pos[c]) > 0:
                    pos[c].popleft()
                if len(pos[c]) == 0:
                    del pos[c]
                l += 1

            if len(pos) == 6 and len(pos['#']) == k:
                lmst = 1010101010
                for ky in 'aeiou#':
                    idx = 0 if ky == '#' else -1
                    if len(pos[ky]) != 0:
                        lmst = min(lmst, pos[ky][idx])
                ans += max(lmst - l + 1, 0)

        return ans
