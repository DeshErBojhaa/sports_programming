# 1146. Snapshot Array
from bisect import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.d = [{0:0} for _ in range(length)]
        self.snapid = 0

    def set(self, index: int, val: int) -> None:        
        self.d[index][self.snapid] = val
        

    def snap(self) -> int:    
        self.snapid += 1
        return self.snapid - 1

    def get(self, index: int, snap_id: int) -> int:
        dic = self.d[index]
        if snap_id in dic:
            return dic[snap_id]
        keys = sorted(dic.keys())
        i = bisect(keys, snap_id)
        return dic[keys[i-1]]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

