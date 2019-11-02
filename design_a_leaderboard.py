# Benjamin Wiens
# Design a Leaderboard (https://leetcode.com/problems/design-a-leaderboard/)

from collections import Counter
class Leaderboard:

    def __init__(self):
        self.hmap = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.hmap:
            self.hmap[playerId] = score
        else:
            self.hmap[playerId] += score

    def top(self, K: int) -> int:
        i = 0
        total = 0
        for key, value in self.hmap.most_common(K):
            total += value
        return total
    
    def reset(self, playerId: int) -> None:
        self.hmap[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
