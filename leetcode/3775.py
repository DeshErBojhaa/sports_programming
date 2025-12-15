class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split(' ')
        vc = lambda w: sum(1 for x in w if x in 'aeiou')
        cnt = vc(w[0])
        for i, x in enumerate(w[1:], 1):
            if vc(x) != cnt:
                continue
            w[i] = w[i][::-1]
        return ' '.join(w)
