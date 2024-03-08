from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]*len(s)
        sum_=0

        for i in range(len(s)):
            if s[i]=='|':
                sum_+=1
            prefix[i]=sum_
        answer = []

        for query in queries:
            first, second = query
            left=right=0
            if s[first]=="|":
                left=first
            else:
                left=min(bisect_right(prefix,prefix[first]),len(s)-1)
            if s[second]=="|":
                right=second
            else:
                right=max(bisect_left(prefix,prefix[second]),0)
            ans=right-left-(prefix[right]-prefix[left])
            answer.append(max(0,ans))
        return answer
