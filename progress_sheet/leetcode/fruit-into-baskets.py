class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        global_max=float('-inf')
        variant=defaultdict(int)
        left=0
        for right in range(len(fruits)):
            variant[fruits[right]]+=1
            if len(variant)<3:
                ans=right-left+1
                global_max=max(global_max,ans)
            else:
                while len(variant)>2 and left<=right:
                    variant[fruits[left]]-=1 
                    if variant[fruits[left]]==0:
                        variant.pop(fruits[left]) 
                    left+=1

        return  global_max                
        