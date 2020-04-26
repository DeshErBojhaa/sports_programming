class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        left_to_right = [1] * N
        right_to_left = [1] * N
        
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                left_to_right[i] = left_to_right[i-1] + 1
        
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right_to_left[i] = right_to_left[i+1] + 1
        
        return sum(max(a,b) for a,b in zip(left_to_right, right_to_left))
