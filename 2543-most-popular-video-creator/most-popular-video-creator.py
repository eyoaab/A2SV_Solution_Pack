class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        def getId(packed):
            packed.sort(key=lambda x:(-x[1],x[0]))
            return packed[0][0]



        binded = defaultdict(list)
        popularity = defaultdict(int)    

        for i in range(len(ids)):
            binded[creators[i]].append([ids[i],views[i]])

            popularity[creators[i]] +=  views[i]

        maxView = max(popularity.values())


        maxPopular = [name for name,view in popularity.items() if view == maxView ]

        return [[name,getId(binded[name])] for name in maxPopular] 





