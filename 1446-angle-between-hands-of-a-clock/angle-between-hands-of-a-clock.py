class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        hour_degree = hour * 30
        minute_degree = minutes * 6
        hour_minute_degree = minutes * 0.5
        hour_total = hour_degree + hour_minute_degree

        angle = abs(minute_degree - hour_total)

        return min(angle, 360 - angle)