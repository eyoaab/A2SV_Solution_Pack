class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        count = Counter(s)
        for char,val in count.items():
            heappush(heap,(-val,char))

        prev_count, prev_char = 0, ''
        result = [] 

        while heap:
            count,char = heappop(heap)
            result.append(char)

            if prev_count < 0:
                heappush(heap, (prev_count, prev_char))  

            prev_count, prev_char = count + 1,char

        result = ''.join(result)

        if len(result) != len(s):
            return ''

        return result              