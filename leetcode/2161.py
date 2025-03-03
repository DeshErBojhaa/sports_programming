class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s, p, b = [], [], []
        for n in nums:
            if n < pivot:
                s.append(n)
                continue
            if n > pivot:
                b.append(n)
                continue
            p.append(n)
        
        return s + p + b
