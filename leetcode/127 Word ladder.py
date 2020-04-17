from collections import defaultdict
from queue import SimpleQueue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = SimpleQueue()
        wl = set([beginWord] + wordList)
        g = defaultdict(list)
        l = len(beginWord)
        
        for w in wl:
            for i in range(l):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nw = w[:i] + c + w[i+1:]
                    if nw == w or nw not in wl:
                        continue
                    g[w].append(nw)
                    g[nw].append(w)
        
        q.put((beginWord, 1))
        seen = set([beginWord])
        while q.qsize():
            w, dist = q.get()
            for nw in g[w]:
                if nw == endWord:
                    return dist + 1
                # print(w, '->', nw)
                if nw in seen:
                    continue
                seen.add(nw)
                q.put((nw, dist+1))
        
        return 0
