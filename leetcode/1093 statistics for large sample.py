class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total_n = sum(count)
        total_s = sum(c*i for i, c in enumerate(count))
        min_, max_ = -1, -1
        for i, c in enumerate(count):
            if min_ == -1 and c:
                min_ = i
            if c:
                max_ = i
        avg = total_s/total_n
        mode = count.index(max(count))
        median = 0
        
        def get_nth_val(n):
            for i in range(len(count)):
                if count[i] > n:
                    return i
                n -= count[i]
            
        if total_n%2:
            median = get_nth_val(total_n//2)
        else:
            
            median = (get_nth_val(total_n//2) + get_nth_val((total_n//2)-1))/2.
        
        return [min_, max_, avg, median, mode]
