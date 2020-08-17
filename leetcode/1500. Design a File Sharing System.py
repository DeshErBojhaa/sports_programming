# 1500. Design a File Sharing System
class FileSharing:

    def __init__(self, m: int):
        self.user_chunk = defaultdict(set)
        self.chunk_user = defaultdict(set)
        self.available_ids = list(range(1, m))
        heapify(self.available_ids)
        

    def join(self, ownedChunks: List[int]) -> int:
        id_ = heappop(self.available_ids)
        chunks = set(ownedChunks)
        
        self.user_chunk[id_].update(chunks)
        for cid in chunks:
            self.chunk_user[cid].add(id_)
        
        return id_
    

    def leave(self, userID: int) -> None:
        chunks = self.user_chunk[userID]
        for cid in chunks:
            self.chunk_user[cid].discard(userID)
        del self.user_chunk[userID]
        heappush(self.available_ids, userID)
        

    def request(self, userID: int, chunkID: int) -> List[int]:
        users = sorted(self.chunk_user[chunkID])
        if users:
            self.user_chunk[userID].add(chunkID)
            self.chunk_user[chunkID].add(userID)
            # users.add(userID)
        return users


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)
