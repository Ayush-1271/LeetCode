class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def dateToDay(date: str)->int:
            month = int(date[:2])
            day = int(date[3:])
            return sum(months[:month-1]) + day
        
        aa = dateToDay(arriveAlice)
        la = dateToDay(leaveAlice)
        ab = dateToDay(arriveBob)
        lb = dateToDay(leaveBob)

        start = max(aa, ab)
        end = min(la, lb)
        return max(0, end-start+1)