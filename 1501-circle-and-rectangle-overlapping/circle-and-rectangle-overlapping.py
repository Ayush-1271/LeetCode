class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def cal_dis(s, e, c):
            if s <= c <= e:
                return 0
            if c < s:
                return s-c
            else:
                return c-e
        
        x_d = cal_dis(x1, x2, xCenter)
        y_d = cal_dis(y1, y2, yCenter)
        d = x_d ** 2 + y_d ** 2
        return d <= (radius ** 2)