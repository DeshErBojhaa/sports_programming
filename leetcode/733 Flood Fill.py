from queue import SimpleQueue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = SimpleQueue()
        
        q.put((sr,sc))
        col = image[sr][sc]
        image[sr][sc] = newColor
        s = set((sr,sc))
        
        while q.qsize():
            r,c = q.get()
            
            for dr, dc in zip([0,-1,0,1], [-1,0,1,0]):
                nr = r + dr
                nc = c + dc
                
                if (nr, nc) in s or nr < 0 or nr >= len(image) or nc < 0 or nc >= len(image[0]) or image[nr][nc] != col:
                    continue
                image[nr][nc] = newColor
                q.put((nr, nc))
                s.add((nr, nc))
        return image
