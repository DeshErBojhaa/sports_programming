def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis = sum(abs(x) for x in target)
        
        for g in ghosts:
            if abs(g[0]-target[0]) + abs(g[1] - target[1]) <= dis:
                return False
            
        return True
