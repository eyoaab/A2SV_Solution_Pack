class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        right = len(skill) - 1
        left = 0

        skill.sort()
        value = skill[left] +  skill[right]


        ans = 0

        
        while left < right:


            if skill[left] +  skill[right] != value:
                return -1

            ans += skill[left] *  skill[right] 

            left += 1
            right -= 1

        return ans       