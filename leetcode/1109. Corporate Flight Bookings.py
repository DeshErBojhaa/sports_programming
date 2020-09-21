# 1109. Corporate Flight Bookings
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        freq = [0] * (n+1)
        
        for a,b,c in bookings:
            freq[a-1] += c
            freq[b] -= c
        
        return list(accumulate(freq))[:-1]
