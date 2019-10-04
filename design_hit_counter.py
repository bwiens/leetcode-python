# Benjamin Wiens
# Design Hit Counter (https://leetcode.com/problems/design-hit-counter/)

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = {}
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.hmap:
            self.hmap[timestamp] = 1
        else:
            self.hmap[timestamp] += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        hits = 0
        for key, value in self.hmap.items():
            #print(timestamp-300, key, value)
            if key >= timestamp - 299 and key <= timestamp:
                hits += value
        return hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
