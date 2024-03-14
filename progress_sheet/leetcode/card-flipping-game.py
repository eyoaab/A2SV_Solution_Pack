class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        bad=set()
        possible=set()
        
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                bad.add(fronts[i])
                if fronts[i] in possible:
                    possible.remove(fronts[i])
            else:
                if not fronts[i] in bad:
                    possible.add(fronts[i])
                if not backs[i] in bad:
                    possible.add(backs[i])

        if possible:
            return min(possible)
        return 0           


        