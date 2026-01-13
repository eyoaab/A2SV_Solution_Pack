class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        minY = min(y for _,y,_ in squares)
        maxY = max(y+l for _,y,l in squares)

        reqArea = sum(l**2 for _,_,l in squares) / 2

        def getArea(mid):
            area = 0

            for x,y,l in squares:
                if y > mid:
                    continue

                y1 = y + l

                if mid > y and mid < y1:
                    area += (mid - y) * l
                elif mid >= y1:
                    area += l ** 2
            return area

        for _ in range(100):
            mid = (maxY + minY) / 2

            area = getArea(mid)
            
            if area < reqArea:
                minY = mid
            else:
                maxY = mid

        return minY