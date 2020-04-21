from collections import defaultdict
from copy import copy
from queue import SimpleQueue
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        g, _g = defaultdict(list), defaultdict(list)
        wordList = set(wordList)
        wordList.discard(beginWord)
        for w in wordList:
            for i in range(len(beginWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nw = w[:i] + c + w[i+1:]
                    if nw == w or nw not in wordList:
                        continue
                    g[w].append(nw)
                    _g[nw].append(w)

        # Make edges from the begin word
        for i in range(len(beginWord)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nw = beginWord[:i] + c + beginWord[i+1:]
                if nw == beginWord or nw not in wordList:
                    continue
                g[beginWord].append(nw)
                _g[nw].append(beginWord)
        
        dis = defaultdict(int)
        
        q = SimpleQueue()
        q.put(beginWord)
        dis[beginWord] = 0
        while not q.empty():
            cur = q.get()
            dist = dis[cur]
            
            for nxt in g[cur]:
                if nxt in dis:
                    continue
                dis[nxt] = dist + 1
                q.put(nxt)
        
        ans = []
        def find_path(cur, path):
            if cur == beginWord:
                ans.append([cur] + path[::-1])
                return
            
            for prev in _g[cur]:
                if dis[prev]+1 == dis[cur]:
                    find_path(prev, path + [cur])
            return
        
        find_path(endWord, [])
        return ans
