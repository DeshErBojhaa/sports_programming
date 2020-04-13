from collections import Counter
class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        p = p.replace('!', ' ').replace('?', ' ').replace("'", ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ')
        bad = set([x.lower() for x in banned])
        c = Counter([x.lower() for x in p.split() if x.lower() not in bad ])
        return c.most_common(1)[0][0]
