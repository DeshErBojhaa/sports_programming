class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_degree = 6 * minutes * 1.0
        
        hour_degree = 30 * hour * 1.0
        
        additional_hour_degree_from_minute = (minutes / 2) * 1.0
        
        hour_degree += additional_hour_degree_from_minute
        
        return min(360 - abs(hour_degree - minute_degree), abs(hour_degree - minute_degree))
