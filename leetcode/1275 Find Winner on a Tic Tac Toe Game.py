
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a, b = set(), set()
        
        for i, v in enumerate(moves):
            if i % 2 == 0:
                a.add((v[0],v[1]))
            else:
                b.add((v[0],v[1]))
        
        
        def check(player):
            s = a
            if player == 'B':
                s = b
            
            for r in range(3):   #  Horizontal
                ok = True
                for c in range(3):
                    if (r,c) not in s:
                        ok = False
                        break
                if ok:
                    return player
            
            for c in range(3):   #  Vertical
                ok = True
                for r in range(3):
                    if (r,c) not in s:
                        ok = False
                        break
                if ok:
                    return player
            
            ok = True
            for i in [(0,0), (1,1), (2,2)]:
                if i not in s:
                    ok = False
                    break
            if ok:
                return player
            
            ok = True
            for i in [(2,0), (1,1), (0,2)]:
                if i not in s:
                    ok = False
                    break
            if ok:
                return player
            return None
        
        if check('A'):
            return 'A'
        if check('B'):
            return 'B'
        
        if len(moves) < 9:
            return "Pending"
        
        return 'Draw'
