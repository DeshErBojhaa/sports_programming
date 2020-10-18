from queue import PriorityQueue
class Solution:
    def findMaximizedCapital(self, k: int, W: int, P: List[int], C: List[int]) -> int:
        min_heap = PriorityQueue()
        max_heap = PriorityQueue()
        for c, p in zip(C,P):
            min_heap.put((c,p))
        # print('Q Size',min_heap.qsize())
        turn = 0
        while turn < k:
            while min_heap.qsize():
                top = min_heap.get()
                # print(top)
                if top[0] > W: # This task costs more than our current capital
                    min_heap.put(top) # Put it back
                    break
                max_heap.put(-top[1])
            if max_heap.qsize():
                W += (-max_heap.get())
            turn += 1
        return W
