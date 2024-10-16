class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0:
            heappush(heap, (-a, 'a'))
        if b > 0:
            heappush(heap, (-b, 'b'))
        if c > 0:
            heappush(heap, (-c, 'c'))

        result = []

        while heap:
            count,char = heappop(heap)

            if len(result) >= 2 and (result[-1] == result[-2] == char):
                if heap:
                    newcount,newchar = heappop(heap)
                    result.append(newchar)

                    heappush(heap,(count,char))

                    if newcount + 1 < 0:
                        heappush(heap,(newcount + 1,newchar))
                else:
                    break 
            else:
                result.append(char)
                count += 1

                if count < 0:
                    heappush(heap,(count,char))

        return ''.join(result)            
