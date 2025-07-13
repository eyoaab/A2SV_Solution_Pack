class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        player = 0
        trainer = 0 
        P = len(players)
        T = len(trainers)

        Count = 0

        while player < P and trainer < T:
            
            if players[player] <= trainers[trainer]:
                
                Count += 1
                player += 1
                trainer += 1

            else:
                trainer += 1

        return Count        

