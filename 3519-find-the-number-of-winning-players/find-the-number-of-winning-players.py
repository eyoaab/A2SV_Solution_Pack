class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        player_list = defaultdict(lambda: [0]*11)
        for player, color in pick:
            player_list[player][color] += 1
        ans = 0
        for player in player_list:
            if max(player_list[player]) > player:
                ans += 1
        return ans