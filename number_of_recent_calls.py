# Benjamin Wiens
# Number of Recent Calls (https://leetcode.com/problems/number-of-recent-calls)

from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        #pop those that can be eliminated
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
