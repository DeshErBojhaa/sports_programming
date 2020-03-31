from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        component = ''.join(map(chr, range(1001)))
        for a, b in edges:
            if component[a] == component[b]:
                return [a,b]
            component = component.replace(component[a], component[b])
