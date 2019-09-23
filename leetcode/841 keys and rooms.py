def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n, cnt = len(rooms), 0
        flag = [False] * n
        
        def trav(cur):
            if flag[cur]:
                return
            flag[cur] = True
            for nxt in rooms[cur]:
                trav(nxt)
        
        trav(0)
        return all(flag)
