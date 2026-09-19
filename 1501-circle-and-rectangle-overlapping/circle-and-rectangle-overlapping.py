class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xi,yi = 0,0

        if x1 > xCenter:
            xi = x1
        elif x2 < xCenter:
            xi = x2
        else:
            xi = xCenter      

        if y1 > yCenter:
            yi = y1
        elif y2 < yCenter:
            yi = y2
        else:
            yi = yCenter      


        distance = (((xi - xCenter) ** 2) + ((yi - yCenter) ** 2) ) ** 0.5

        return distance <= radius       