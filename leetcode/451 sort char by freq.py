def frequencySort(self, s: str) -> str:
        c = Counter(s)
        s = ''
        for k ,v in reversed(sorted(c.items(), key=operator.itemgetter(1))):
            s += k*v
        return s
