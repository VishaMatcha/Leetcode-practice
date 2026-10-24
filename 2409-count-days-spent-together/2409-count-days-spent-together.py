class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day_of_year(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month - 1]) + day
            
        a_arrive = to_day_of_year(arriveAlice)
        a_leave = to_day_of_year(leaveAlice)
        b_arrive = to_day_of_year(arriveBob)
        b_leave = to_day_of_year(leaveBob)
        
        overlap_start = max(a_arrive, b_arrive)
        overlap_end = min(a_leave, b_leave)
        
        return max(0, overlap_end - overlap_start + 1)
