class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        heap = [(-i, -count) for i, count in enumerate(freq) if count > 0]
        heapify(heap)
        ans = []
        while heap:
            ch, count = heappop(heap)
            count = -count
            use = min(repeatLimit, count)
            ans.append(chr(-ch + ord('a')) * use)
            count -= use
            if count > 0:
                if heap:
                    nextCh, nextCount = heappop(heap)
                    ans.append(chr(-nextCh + ord('a')))
                    if nextCount + 1 < 0:
                        heappush(heap, (nextCh, nextCount + 1))
                    heappush(heap, (ch, -count))
        return ''.join(ans)